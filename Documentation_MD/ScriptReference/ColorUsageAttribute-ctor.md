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

# ColorUsageAttribute Constructor

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

public ColorUsageAttribute(bool showAlpha);

## Declaration

public ColorUsageAttribute(bool showAlpha, bool hdr);

**Obsolete** Brightness and exposure parameters are no longer used for
anything. Use ColorUsageAttribute(bool showAlpha, bool hdr).

## Declaration

public ColorUsageAttribute(bool showAlpha, bool hdr, float minBrightness,
float maxBrightness, float minExposureValue, float maxExposureValue);

### Parameters

showAlpha | If false then the alpha channel info is hidden both in the ColorField and in the Color Picker.  
---|---  
hdr | Set to true if the color should be treated as a HDR color (default value: false).  
minBrightness | Minimum allowed HDR color component value when using the HDR Color Picker (default value: 0).  
maxBrightness | Maximum allowed HDR color component value when using the HDR Color Picker (default value: 8).  
minExposureValue | Minimum exposure value allowed in the HDR Color Picker (default value: 1/8 = 0.125).  
maxExposureValue | Maximum exposure value allowed in the HDR Color Picker (default value: 3).  
  
### Description

Attribute for Color fields. Used for configuring the GUI for the color.

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

