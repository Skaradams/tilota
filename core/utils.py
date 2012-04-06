# -*- coding: utf-8 *-*
import uuid
import zmq
from tilota import settings
from tilota.core.console import Console


def create_new_game(game_cmd):
    tmp_ipc = 'ipc://%s/%s.ipc' % (settings.IPC_PATH, str(uuid.uuid1()))
    tmp_socket = zmq.Socket(zmq.Context(), zmq.PULL)
    tmp_socket.bind(tmp_ipc)
    daemon_socket = zmq.Socket(zmq.Context(), zmq.PUSH)
    daemon_socket.connect(settings.DAEMON_INBOX)
    game = Console('dmtcp_checkpoint %s' % game_cmd)
    daemon_socket.send_json(
        {'name': 'get_game_id', 'pid': game.process.pid, 'reply_ipc': tmp_ipc}
    )
    game_id = tmp_socket.recv_json()
    daemon_socket.send_json({'name': 'save_checkpoints', 'reply_ipc': tmp_ipc})
    tmp_socket.recv_json()
    return game_id
