[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

# PhotoCapture

class in UnityEngine.Windows.WebCam

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

### Description

Captures a photo from the web camera and stores it in memory or on disk.

Demonstrates how to take a photo using the PhotoCapture functionality and
display it on a Unity GameObject.

    
    
    using UnityEngine;
    using System.Collections;
    using System.Linq;
    using UnityEngine.Windows.WebCam;  
      
    public class PhotoCaptureExample : [MonoBehaviour](MonoBehaviour.html)
    {
        [PhotoCapture](Windows.WebCam.PhotoCapture.html) photoCaptureObject = null;
        [Texture2D](Texture2D.html) targetTexture = null;  
      
        // Use this for initialization
        void Start()
        {
            [Resolution](Resolution.html) cameraResolution = PhotoCapture.SupportedResolutions.OrderByDescending((res) => res.width * res.height).First();
            targetTexture = new [Texture2D](Texture2D.html)(cameraResolution.width, cameraResolution.height);  
      
            // Create a [PhotoCapture](Windows.WebCam.PhotoCapture.html) object
            [PhotoCapture.CreateAsync](Windows.WebCam.PhotoCapture.CreateAsync.html)(false, delegate([PhotoCapture](Windows.WebCam.PhotoCapture.html) captureObject) {
                photoCaptureObject = captureObject;
                [CameraParameters](Windows.WebCam.CameraParameters.html) cameraParameters = new [CameraParameters](Windows.WebCam.CameraParameters.html)();
                cameraParameters.hologramOpacity = 0.0f;
                cameraParameters.cameraResolutionWidth = cameraResolution.width;
                cameraParameters.cameraResolutionHeight = cameraResolution.height;
                cameraParameters.pixelFormat = [CapturePixelFormat.BGRA32](Windows.WebCam.CapturePixelFormat.BGRA32.html);  
      
                // Activate the camera
                photoCaptureObject.StartPhotoModeAsync(cameraParameters, delegate(PhotoCapture.PhotoCaptureResult result) {
                    // Take a picture
                    photoCaptureObject.TakePhotoAsync(OnCapturedPhotoToMemory);
                });
            });
        }  
      
        void OnCapturedPhotoToMemory(PhotoCapture.PhotoCaptureResult result, [PhotoCaptureFrame](Windows.WebCam.PhotoCaptureFrame.html) photoCaptureFrame)
        {
            // Copy the raw image data into our target texture
            photoCaptureFrame.UploadImageDataToTexture(targetTexture);  
      
            // Create a gameobject that we can apply our texture to
            [GameObject](GameObject.html) quad = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Quad](PrimitiveType.Quad.html));
            [Renderer](Renderer.html) quadRenderer = quad.GetComponent<[Renderer](Renderer.html)>() as [Renderer](Renderer.html);
            quadRenderer.material = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Unlit/[Texture](Texture.html)"));  
      
            quad.transform.parent = this.transform;
            quad.transform.localPosition = new [Vector3](Vector3.html)(0.0f, 0.0f, 3.0f);  
      
            quadRenderer.material.SetTexture("_MainTex", targetTexture);  
      
            // Deactivate our camera
            photoCaptureObject.StopPhotoModeAsync(OnStoppedPhotoMode);
        }  
      
        void OnStoppedPhotoMode(PhotoCapture.PhotoCaptureResult result)
        {
            // Shutdown our photo capture resource
            photoCaptureObject.Dispose();
            photoCaptureObject = null;
        }
    }
    

### Static Properties

[SupportedResolutions](Windows.WebCam.PhotoCapture.SupportedResolutions.html)|
A list of all the supported device resolutions for taking pictures.  
---|---  
  
### Public Methods

[Dispose](Windows.WebCam.PhotoCapture.Dispose.html)| Dispose must be called to
shutdown the PhotoCapture instance.  
---|---  
[GetUnsafePointerToVideoDeviceController](Windows.WebCam.PhotoCapture.GetUnsafePointerToVideoDeviceController.html)|
Provides a COM pointer to the native IVideoDeviceController.  
[StartPhotoModeAsync](Windows.WebCam.PhotoCapture.StartPhotoModeAsync.html)|
Asynchronously starts photo mode.  
[StopPhotoModeAsync](Windows.WebCam.PhotoCapture.StopPhotoModeAsync.html)|
Asynchronously stops photo mode.  
[TakePhotoAsync](Windows.WebCam.PhotoCapture.TakePhotoAsync.html)|
Asynchronously captures a photo from the web camera and saves it to disk.  
  
### Static Methods

[CreateAsync](Windows.WebCam.PhotoCapture.CreateAsync.html)| Asynchronously
creates an instance of a PhotoCapture object that can be used to capture
photos.  
---|---  
  
### Delegates

[OnCapturedToDiskCallback](Windows.WebCam.PhotoCapture.OnCapturedToDiskCallback.html)|
Called when a photo has been saved to the file system.  
---|---  
[OnCapturedToMemoryCallback](Windows.WebCam.PhotoCapture.OnCapturedToMemoryCallback.html)|
Called when a photo has been captured to memory.  
[OnCaptureResourceCreatedCallback](Windows.WebCam.PhotoCapture.OnCaptureResourceCreatedCallback.html)|
Called when a PhotoCapture resource has been created.  
[OnPhotoModeStartedCallback](Windows.WebCam.PhotoCapture.OnPhotoModeStartedCallback.html)|
Called when photo mode has been started.  
[OnPhotoModeStoppedCallback](Windows.WebCam.PhotoCapture.OnPhotoModeStoppedCallback.html)|
Called when photo mode has been stopped.  
  
Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

