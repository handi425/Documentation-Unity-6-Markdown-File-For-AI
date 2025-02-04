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

#
[PhotoCaptureFrame](Windows.WebCam.PhotoCaptureFrame.html).CopyRawImageDataIntoBuffer

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

## Declaration

public void CopyRawImageDataIntoBuffer(List<byte> byteBuffer);

### Parameters

byteBuffer | The destination byte list to which the raw captured image data will be copied to.  
---|---  
  
### Description

Will copy the raw IMFMediaBuffer image data into a byte list.

If you would like to do your own image processing on the byte data in an
external plugin or on another thread, you may want to copy the raw
IMFMediaBuffer data into your own byte list.  
  
For more information about the WinRT IMFMediaBuffer object, please vist
<https://msdn.microsoft.com/en-
us/library/windows/desktop/ms696261(v=vs.85).aspx>  
  
This example will capture an Image from the Web Camera and manually copy the
image data out of a raw IMFMediaBuffer object into a Texture and display it on
a GameObject.

    
    
    using UnityEngine;
    using System.Collections;
    using System.Collections.Generic;
    using System.Linq;
    using UnityEngine.Windows.WebCam;  
      
    public class PhotoCaptureRawImageExample : [MonoBehaviour](MonoBehaviour.html)
    {
        [PhotoCapture](Windows.WebCam.PhotoCapture.html) photoCaptureObject = null;
        [Texture2D](Texture2D.html) targetTexture = null;
        [Renderer](Renderer.html) quadRenderer = null;  
      
        // Use this for initialization
        void Start()
        {
            [Resolution](Resolution.html) cameraResolution = PhotoCapture.SupportedResolutions.OrderByDescending((res) => res.width * res.height).First();  
      
            targetTexture = new [Texture2D](Texture2D.html)(cameraResolution.width, cameraResolution.height, [TextureFormat.RGBA32](TextureFormat.RGBA32.html), false);  
      
            [PhotoCapture.CreateAsync](Windows.WebCam.PhotoCapture.CreateAsync.html)(false, delegate([PhotoCapture](Windows.WebCam.PhotoCapture.html) captureObject) {
                photoCaptureObject = captureObject;  
      
                [CameraParameters](Windows.WebCam.CameraParameters.html) c = new [CameraParameters](Windows.WebCam.CameraParameters.html)();
                c.cameraResolutionWidth = targetTexture.width;
                c.cameraResolutionHeight = targetTexture.height;
                c.pixelFormat = [CapturePixelFormat.BGRA32](Windows.WebCam.CapturePixelFormat.BGRA32.html);  
      
                captureObject.StartPhotoModeAsync(c, delegate(PhotoCapture.PhotoCaptureResult result) {
                    photoCaptureObject.TakePhotoAsync(OnCapturedPhotoToMemory);
                });
            });
        }  
      
        void OnCapturedPhotoToMemory(PhotoCapture.PhotoCaptureResult result, [PhotoCaptureFrame](Windows.WebCam.PhotoCaptureFrame.html) photoCaptureFrame)
        {
            List<byte> imageBufferList = new List<byte>();
            // Copy the raw IMFMediaBuffer data into our empty byte list.
            photoCaptureFrame.CopyRawImageDataIntoBuffer(imageBufferList);  
      
            // In this example, we captured the image using the BGRA32 format.
            // So our stride will be 4 since we have a byte for each rgba channel.
            // The raw image data will also be flipped so we access our pixel data
            // in the reverse order.
            int stride = 4;
            float denominator = 1.0f / 255.0f;
            List<[Color](Color.html)> colorArray = new List<[Color](Color.html)>();
            for (int i = imageBufferList.Count - 1; i >= 0; i -= stride)
            {
                float a = (int)(imageBufferList[i - 0]) * denominator;
                float r = (int)(imageBufferList[i - 1]) * denominator;
                float g = (int)(imageBufferList[i - 2]) * denominator;
                float b = (int)(imageBufferList[i - 3]) * denominator;  
      
                colorArray.Add(new [Color](Color.html)(r, g, b, a));
            }  
      
            targetTexture.SetPixels(colorArray.ToArray());
            targetTexture.Apply();  
      
            if (quadRenderer == null)
            {
                [GameObject](GameObject.html) p = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Quad](PrimitiveType.Quad.html));
                quadRenderer = p.GetComponent<[Renderer](Renderer.html)>() as [Renderer](Renderer.html);
                quadRenderer.material = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Custom/Unlit/UnlitTexture"));  
      
                p.transform.parent = this.transform;
                p.transform.localPosition = new [Vector3](Vector3.html)(0.0f, 0.0f, 1.0f);
            }  
      
            quadRenderer.material.SetTexture("_MainTex", targetTexture);  
      
            // Take another photo
            photoCaptureObject.TakePhotoAsync(OnCapturedPhotoToMemory);
        }
    }
    

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

