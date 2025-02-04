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

# DLSSCommandExecutionData

struct in UnityEngine.NVIDIA

/

Implemented in:[UnityEngine.NVIDIAModule](UnityEngine.NVIDIAModule.html)

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

Represents the state of a DLSSContext. If you call Device.ExecuteDLSS, Unity
sends the values in this struct to the runtime. After this, you can change the
values in this struct without any side effects.

### Properties

[invertXAxis](NVIDIA.DLSSCommandExecutionData-invertXAxis.html)| Indicates if
the X axis is inverted. Set to 0 or 1.  
---|---  
[invertYAxis](NVIDIA.DLSSCommandExecutionData-invertYAxis.html)| Indicates if
the Y axis is inverted. Set to 0 or 1.  
[jitterOffsetX](NVIDIA.DLSSCommandExecutionData-jitterOffsetX.html)| The
x-axis jitter camera offset in device coordinates.  
[jitterOffsetY](NVIDIA.DLSSCommandExecutionData-jitterOffsetY.html)| The
y-axis jitter camera offset in device coordinates.  
[mvScaleX](NVIDIA.DLSSCommandExecutionData-mvScaleX.html)| If you set the
DLSSFeatureFlags.MVLowRes flag, this value indicates the scale (smaller) of
the motion vector buffer input texture used in the x-axis.  
[mvScaleY](NVIDIA.DLSSCommandExecutionData-mvScaleY.html)| If you set the
DLSSFeatureFlags.MVLowRes flag, this value indicates the scale (smaller) of
the motion vector buffer input texture used in the y-axis.  
[preExposure](NVIDIA.DLSSCommandExecutionData-preExposure.html)| Specifies a
pre exposure multiplier for the input color texture.  
[reset](NVIDIA.DLSSCommandExecutionData-reset.html)| Indicates whether to
invalidate the history buffers.  
[sharpness](NVIDIA.DLSSCommandExecutionData-sharpness.html)| Specifies how
sharp the frame should look as a value from 0 to 1.  
[subrectHeight](NVIDIA.DLSSCommandExecutionData-subrectHeight.html)| The
subrectangle height of input buffers to use.  
[subrectOffsetX](NVIDIA.DLSSCommandExecutionData-subrectOffsetX.html)| The
subrectangle x-axis offset of input buffers to use.  
[subrectOffsetY](NVIDIA.DLSSCommandExecutionData-subrectOffsetY.html)| The
subrectangle y-axis offset of input buffers to use.  
[subrectWidth](NVIDIA.DLSSCommandExecutionData-subrectWidth.html)| The
subrectangle width of input buffers to use.  
  
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

