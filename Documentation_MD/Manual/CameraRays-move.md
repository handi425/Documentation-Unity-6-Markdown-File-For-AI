[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/CameraRays-move.html)
  * [中文](/cn/current/Manual/CameraRays-move.html)
  * [日本語](/ja/current/Manual/CameraRays-move.html)
  * [한국어](/kr/current/Manual/CameraRays-move.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/CameraRays-move.html)
  * [中文](/cn/current/Manual/CameraRays-move.html)
  * [日本語](/ja/current/Manual/CameraRays-move.html)
  * [한국어](/kr/current/Manual/CameraRays-move.html)

  * [Working in Unity](working-in-unity.html)
  * [Cameras](Cameras.html)
  * [The camera view](CameraView.html)
  * [Rays from the camera](CameraRays.html)
  * Move a camera along a ray

[](CameraRays-cast.html)

Cast a ray from a camera

[](MultipleCameras-landing.html)

Using multiple cameras

# Move a camera along a ray

It is sometimes useful to get a ray corresponding to a screen position and
then move the **camera** A component which creates an image of a particular
viewpoint in your scene. The output is either drawn to the screen or captured
as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) along that ray. For example, you may
want to allow the user to select an object with the mouse and then zoom in on
it while keeping it “pinned” to the same screen position under the mouse (this
might be useful when the camera is looking at a tactical map, for example).
The code to do this is fairly straightforward:

    
    
    using UnityEngine;
    using System.Collections;
    
    public class ExampleScript : MonoBehaviour {
        public bool zooming;
        public float zoomSpeed;
        public Camera camera;
    
        void Update() {
            if (zooming) {
                Ray ray = camera.ScreenPointToRay(Input.mousePosition);
                float zoomDistance = zoomSpeed * Input.GetAxis("Vertical") * Time.deltaTime;
                camera.transform.Translate(ray.direction * zoomDistance, Space.World);
            }
        }
    }
    

[](CameraRays-cast.html)

Cast a ray from a camera

[](MultipleCameras-landing.html)

Using multiple cameras

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

