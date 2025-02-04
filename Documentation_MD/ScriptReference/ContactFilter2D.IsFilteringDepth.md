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

#  [ContactFilter2D](ContactFilter2D.html).IsFilteringDepth

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

public bool IsFilteringDepth([GameObject](GameObject.html) obj);

### Parameters

obj | The [GameObject](GameObject.html) used to check the z-position (depth) of [Transform.position](Transform-position.html).  
---|---  
  
### Returns

**bool** Returns true when `obj` is excluded by the filter and false if
otherwise.

### Description

Checks if the [Transform](Transform.html) for `obj` is within the depth range
to be filtered.

Filtering is defined as including or excluding objects based upon a specific
condition. Depth filtering checks the z-position of a
[GameObject](GameObject.html) [Transform.position](Transform-position.html)
and includes it when it is within the depth range and excludes it if
otherwise. IsFilteringDepth returns true when
[useDepth](ContactFilter2D-useDepth.html) is set to true and the `obj`
transform's z-position is outside the depth defined by
[minDepth](ContactFilter2D-minDepth.html) and
[maxDepth](ContactFilter2D-maxDepth.html). This indicates the `obj` is
filtered which means it should be excluded. IsFilteringDepth returns false if
otherwise. **Note:** : Setting
[useOutsideDepth](ContactFilter2D-useOutsideDepth.html) to true inverts the
function behavior and it returns opposite results. Additional resources:
[useDepth](ContactFilter2D-useDepth.html), ::ref:minDepth &
[maxDepth](ContactFilter2D-maxDepth.html).

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

