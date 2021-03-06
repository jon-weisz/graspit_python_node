
from ros_request_handlers import *


class ROSInterface():

    def __init__(self):
        self.camera_origin_request_handler = CameraOriginRequestHandler()
        self.object_recognition_request_handler = ObjectRecognitionRequestHandler()
        self.check_reachability_request_handler = CheckReachabilityRequestHandler()
        self.execute_grasp_request_handler = ExecuteGraspRequestHandler()

    def handle_object_recognition_request(self):
        response = self.object_recognition_request_handler.handle()
        return response

    def handle_execute_grasp_request(self, request):
        response = self.execute_grasp_request_handler.handle(request)
        return response

    def handle_check_reachability_request(self, request):
        response = self.check_reachability_request_handler.handle(request)
        return response

    def handle_camera_origin_request(self):
        response = self.camera_origin_request_handler.handle()
        return response