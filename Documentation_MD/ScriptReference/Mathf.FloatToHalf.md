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

#  [Mathf](Mathf.html).FloatToHalf

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

[Switch to Manual](../Manual/class-Mathf.html "Go to Mathf Component in the
Manual")

## Declaration

public static ushort FloatToHalf(float val);

### Parameters

val | The floating point value to convert.  
---|---  
  
### Returns

**ushort** The converted half-precision float, stored in a 16-bit unsigned
integer.

### Description

Encode a floating point value into a 16-bit representation.

Converting a floating point value to a half causes it to lose precision and
also reduces the maximum range of values it can represent. The new range is
from -65,504 and 65,504. For more information on 16-bit floating-point
numbers, and for information on how precision changes over the range of
values, see [Half-precision floating-point
format](https://en.wikipedia.org/wiki/Half-precision_floating-point_format).  
  
If the converted floating point value falls exactly between two half-precision
values, this method rounds it to the value furthest from zero (Round away from
zero tie-break rule). This selects the value closer to positive or negative
infinity, depending on the sign.  
  
You should only use the returned ushort as a storage format. If you want to
perform mathematical operations on it, first convert it back to a float with
[Mathf.HalfToFloat](Mathf.HalfToFloat.html).

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

