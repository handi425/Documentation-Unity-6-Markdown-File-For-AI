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

# FSR2CommandExecutionData

struct in UnityEngine.AMD

/

Implemented in:[UnityEngine.AMDModule](UnityEngine.AMDModule.html)

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

Represents the state of a FSR2Context. If you call Device.ExecuteFSR2, Unity
sends the values in this struct to the runtime. After this, you can change the
values in this struct without any side effects.

### Properties

[cameraFar](AMD.FSR2CommandExecutionData-cameraFar.html)| The distance to the
far plane of the camera.  
---|---  
[cameraFovAngleVertical](AMD.FSR2CommandExecutionData-
cameraFovAngleVertical.html)| The camera angle field of view in the vertical
direction (expressed in radians).  
[cameraNear](AMD.FSR2CommandExecutionData-cameraNear.html)| The distance to
the near plane of the camera.  
[enableSharpening](AMD.FSR2CommandExecutionData-enableSharpening.html)| Enable
an additional sharpening pass.  
[frameTimeDelta](AMD.FSR2CommandExecutionData-frameTimeDelta.html)| The time
elapsed since the last frame (expressed in milliseconds).  
[jitterOffsetX](AMD.FSR2CommandExecutionData-jitterOffsetX.html)| The subpixel
jitter offset applied to the camera (X axis).  
[jitterOffsetY](AMD.FSR2CommandExecutionData-jitterOffsetY.html)| The subpixel
jitter offset applied to the camera (Y axis).  
[MVScaleX](AMD.FSR2CommandExecutionData.MVScaleX.html)| The scale factor to
apply to motion vectors (X axis).  
[MVScaleY](AMD.FSR2CommandExecutionData.MVScaleY.html)| The scale factor to
apply to motion vectors (Y axis).  
[preExposure](AMD.FSR2CommandExecutionData-preExposure.html)| The pre exposure
value (must be > 0.0f).  
[renderSizeHeight](AMD.FSR2CommandExecutionData-renderSizeHeight.html)| The
height resolution that was used for rendering the input resources.  
[renderSizeWidth](AMD.FSR2CommandExecutionData-renderSizeWidth.html)| The
width resolution that was used for rendering the input resources.  
[reset](AMD.FSR2CommandExecutionData-reset.html)| A boolean value which when
set to true, indicates the camera has moved discontinuously.  
[sharpness](AMD.FSR2CommandExecutionData-sharpness.html)| The sharpness value
between 0 and 1, where 0 is no additional sharpness and 1 is maximum
additional sharpness.  
  
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

