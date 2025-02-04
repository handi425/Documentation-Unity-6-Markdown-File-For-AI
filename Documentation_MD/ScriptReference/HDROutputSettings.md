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

# HDROutputSettings

class in UnityEngine

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

Provides access to HDR display settings and information.

### Static Properties

[displays](HDROutputSettings-displays.html)| The list of currently connected
displays with possible HDR availability.  
---|---  
[main](HDROutputSettings-main.html)| The HDROutputSettings for the main
display.  
  
### Properties

[active](HDROutputSettings-active.html)| Describes whether HDR output is
currently active on the display. It is true if this is the case, and @@false@
otherwise.  
---|---  
[automaticHDRTonemapping](HDROutputSettings-automaticHDRTonemapping.html)|
Describes whether Unity performs HDR tonemapping automatically.  
[available](HDROutputSettings-available.html)| Describes whether HDR is
currently available on your primary display and that you have HDR enabled in
your Unity Project. It is true if this is the case, and false otherwise.  
[displayColorGamut](HDROutputSettings-displayColorGamut.html)| The ColorGamut
used to output to the active HDR display.  
[format](HDROutputSettings-format.html)| The RenderTextureFormat of the
display buffer for the active HDR display.  
[graphicsFormat](HDROutputSettings-graphicsFormat.html)| The GraphicsFormat of
the display buffer for the active HDR display.  
[HDRModeChangeRequested](HDROutputSettings.HDRModeChangeRequested.html)|
Describes whether the user has requested to change the HDR Output Mode. It is
true if this is the case, and false otherwise.  
[maxFullFrameToneMapLuminance](HDROutputSettings-
maxFullFrameToneMapLuminance.html)| Maximum input luminance at which gradation
is preserved even when the entire screen is bright.  
[maxToneMapLuminance](HDROutputSettings-maxToneMapLuminance.html)| Maximum
input luminance at which gradation is preserved when 10% of the screen is
bright.  
[minToneMapLuminance](HDROutputSettings-minToneMapLuminance.html)| Minimum
input luminance at which gradation is identifiable.  
[paperWhiteNits](HDROutputSettings-paperWhiteNits.html)| The base luminance of
a white paper surface in nits or candela per square meter (cd/m2).  
  
### Public Methods

[RequestHDRModeChange](HDROutputSettings.RequestHDRModeChange.html)| Use this
function to request a change in the HDR Output Mode and in the value of
HDROutputSettings.active.  
---|---  
  
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

