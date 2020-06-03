from vcap import (
    BaseCapsule,
    NodeDescription,
    DeviceMapper,
    common_detector_options
)
from .backend import Backend


class Capsule(BaseCapsule):
    name = "detector_face_openvino"
    description = "CPU-only fast face detector."
    version = 1
    device_mapper = DeviceMapper.map_to_single_cpu()
    input_type = NodeDescription(size=NodeDescription.Size.NONE)
    output_type = NodeDescription(
        size=NodeDescription.Size.ALL,
        detections=["face"])
    backend_loader = lambda capsule_files, device: Backend(
        model_xml=capsule_files["face-detection-adas-0001.xml"],
        weights_bin=capsule_files["face-detection-adas-0001.bin"],
    )
    options = common_detector_options
