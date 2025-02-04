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

# WebCamTexture Constructor

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

public WebCamTexture();

## Declaration

public WebCamTexture(int requestedWidth, int requestedHeight, int
requestedFPS);

## Declaration

public WebCamTexture(int requestedWidth, int requestedHeight);

## Declaration

public WebCamTexture(string deviceName);

## Declaration

public WebCamTexture(string deviceName, int requestedWidth, int
requestedHeight);

## Declaration

public WebCamTexture(string deviceName, int requestedWidth, int
requestedHeight, int requestedFPS);

### Parameters

deviceName | The name of the video input device to be used.  
---|---  
requestedWidth | The requested width of the texture.  
requestedHeight | The requested height of the texture.  
requestedFPS | The requested frame rate of the texture.  
  
### Description

Create a WebCamTexture.

Use [WebCamTexture.devices](WebCamTexture-devices.html) to get a list of the
names of available camera devices. If no device name is supplied to the
constructor or is passed as a null string, the first device found will be
used.  
  
The requested width, height and framerate specified by the parameters may not
be supported by the chosen camera. In such cases, the closest available values
will be used.  
  
Call
[Application.RequestUserAuthorization](Application.RequestUserAuthorization.html)
before creating a WebCamTexture.  
  
**Note:** using webcam texture on Android requires a device running Honeycomb
(Android 3.0) or later.  
  
**Note:** If you want to use a WebCamTexture to play the camera stream from a
device connected through Unity Remote, then you must initialize it through use
of the constructor. It is not possible to change the device later using
[WebCamTexture.deviceName](WebCamTexture-deviceName.html) from a regular
device to a remote device and vice versa.  
  
**Note:** For camera devices of kind
[WebCamKind.ColorAndDepth](WebCamKind.ColorAndDepth.html) (currently these are
only dual back and true depth cameras on latest iOS devices), it is possible
to create a WebCamTexture instance to receive depth data using
[WebCamDevice.depthCameraName](WebCamDevice-depthCameraName.html) as the
deviceName. This WebCamTexture always contains one channel and is in half-
precision floating point format with distance values in meters.  
  
If required, it is also possible to create a second WebCamTexture instance
using [WebCamDevice.name](WebCamDevice-name.html) as deviceName to receive
color data. In this case, both color and depth data will be synchronized.  
  
Currently, iOS supports only limited combinations of color/depth data
resolutions. **requestedWidth** and **requestedHeight** parameters are
ignored, when creating WebCamTexture instances for ColorAndDepth devices. For
iPhone 7+/8+ dual back cameras, the size of the WebCamTexture for color data
is 1440x1080 and for iPhone X dual back and front true depth cameras, it is
1500x1126. The depth data resolution is always a maximum of 320x240 for iPhone
4+/8+/X dual back cameras and 640x480 for iPhone X front true depth cameras.

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

