[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/webgl-browser-access-device.html)
  * [中文](/cn/current/Manual/webgl-browser-access-device.html)
  * [日本語](/ja/current/Manual/webgl-browser-access-device.html)
  * [한국어](/kr/current/Manual/webgl-browser-access-device.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/webgl-browser-access-device.html)
  * [中文](/cn/current/Manual/webgl-browser-access-device.html)
  * [日本語](/ja/current/Manual/webgl-browser-access-device.html)
  * [한국어](/kr/current/Manual/webgl-browser-access-device.html)

  * [Platform development ](PlatformSpecific.html)
  * [Web](webgl.html)
  * [Web development](webgl-develop.html)
  * Web browser access to device features

[](webgl-canvas-size.html)

Configure a Web Canvas size

[](webgl-networking.html)

Web networking

# Web browser access to device features

The Unity Web platform supports [WebCam
access](../ScriptReference/WebCamDevice.html). To allow a Web application to
access the webcam on a device, the browser must request its user to provide
access to the **camera** A component which creates an image of a particular
viewpoint in your scene. The output is either drawn to the screen or captured
as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera). Without the permission to access the
camera, the browser returns incomplete or inaccurate information.

**Note:** Currently, the Web platform supports WebCam devices only.

To request browser permission to access the webcam, use the
`Application.RequestUserAuthorization` API:

    
    
    using UnityEngine;
    using UnityEngine.iOS;
    using System.Collections;
    
    // Get WebCam information from the browser
    public class ExampleClass : MonoBehaviour
    {
        private WebCamDevice[] devices;
        
        // Use this for initialization
        IEnumerator Start()
        {
            yield return Application.RequestUserAuthorization(UserAuthorization.WebCam);
            if (Application.HasUserAuthorization(UserAuthorization.WebCam))
            {
                Debug.Log("webcam found");
                devices = WebCamTexture.devices;
                for (int cameraIndex = 0; cameraIndex < devices.Length; ++cameraIndex)
                {
                    Debug.Log("devices[cameraIndex].name: ");
                    Debug.Log(devices[cameraIndex].name);
                    Debug.Log("devices[cameraIndex].isFrontFacing");
                    Debug.Log(devices[cameraIndex].isFrontFacing);
                }
            }
            else
            {
                Debug.Log("no webcams found");
            }
        }
    }
    

**Note:** Unity recommends to use the `MediaDevices.getUserMedia()` API to
request user permission for accessing the device. This feature is available
only in secure contexts (HTTPS).

[](webgl-canvas-size.html)

Configure a Web Canvas size

[](webgl-networking.html)

Web networking

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

