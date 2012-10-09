import unittest
import mock

def echo_data(socket):
    data = socket.recv()
    socket.send(data)

class MyTest(unittest.TestCase):

    def test_send_recv(self):
        socket = mock.Mock()
        socket.recv.return_value = 'Some data'
        echo_data(socket)
        socket.send.assert_called_with('Some data')

if __name__ == '__main__':
    unittest.main()
