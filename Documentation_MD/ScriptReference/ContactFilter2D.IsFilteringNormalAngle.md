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

#  [ContactFilter2D](ContactFilter2D.html).IsFilteringNormalAngle

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

public bool IsFilteringNormalAngle([Vector2](Vector2.html) normal);

### Parameters

normal | The normal used to calculate an angle.  
---|---  
  
### Returns

**bool** Returns true when `normal` is excluded by the filter and false if
otherwise.

### Description

Checks if the angle of `normal` is within the normal angle range to be
filtered.

Filtering is defined as including or excluding objects based upon a specific
condition. Normal angle filtering checks an angle and includes it when it is
within the normal angle range and excludes it if otherwise.
IsFilteringNormalAngle returns true when
[useNormalAngle](ContactFilter2D-useNormalAngle.html) is set to true and the
angle is outside the normal angle range defined by
[minNormalAngle](ContactFilter2D-minNormalAngle.html) and
[maxNormalAngle](ContactFilter2D-maxNormalAngle.html). This indicates the
angle is filtered which means it should be excluded. IsFilteringNormalAngle
returns false if otherwise. **Note:** : Setting
[useOutsideNormalAngle](ContactFilter2D-useOutsideNormalAngle.html) to true
inverts the function behavior and it returns opposite results. Additional
resources: [useNormalAngle](ContactFilter2D-useNormalAngle.html),
::ref:minNormalAngle & [maxNormalAngle](ContactFilter2D-maxNormalAngle.html).

* * *

## Declaration

public bool IsFilteringNormalAngle(float angle);

### Parameters

angle | The angle used for comparison in the filter.  
---|---  
  
### Returns

**bool** Returns true when `angle` is excluded by the filter and false if
otherwise.

### Description

Checks if the `angle` is within the normal angle range to be filtered.

Filtering is defined as including or excluding objects based upon a specific
condition. Normal angle filtering checks an angle and includes it when it is
within the normal angle range and excludes it if otherwise.
IsFilteringNormalAngle returns true when
[useNormalAngle](ContactFilter2D-useNormalAngle.html) is set to true and the
angle is outside the normal angle range defined by
[minNormalAngle](ContactFilter2D-minNormalAngle.html) and
[maxNormalAngle](ContactFilter2D-maxNormalAngle.html). This indicates the
angle is filtered which means it should be excluded. IsFilteringNormalAngle
returns false if otherwise. **Note:** : Setting
[useOutsideNormalAngle](ContactFilter2D-useOutsideNormalAngle.html) to true
inverts the function behavior and it returns opposite results. Additional
resources: [useNormalAngle](ContactFilter2D-useNormalAngle.html),
::ref:minNormalAngle & [maxNormalAngle](ContactFilter2D-maxNormalAngle.html).

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

