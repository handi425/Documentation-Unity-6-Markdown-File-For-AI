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

#  [CullingGroup](CullingGroup.html).QueryIndices

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

public int QueryIndices(bool visible, int[] result, int firstIndex);

## Declaration

public int QueryIndices(int distanceIndex, int[] result, int firstIndex);

## Declaration

public int QueryIndices(bool visible, int distanceIndex, int[] result, int
firstIndex);

### Parameters

visible | True if only visible spheres should be retrieved; false if only invisible spheres should be retrieved.  
---|---  
distanceIndex | The distance band that retrieved spheres must be in.  
result | An array that will be filled with the retrieved sphere indices.  
firstIndex | The index of the sphere to begin searching at.  
  
### Returns

**int** The number of sphere indices found and written into the result array.

### Description

Retrieve the indices of spheres that have particular visibility and/or
distance states.

Use the overload that corresponds to the state properties you are interested
in. For example, if you want to retrieve visible spheres in any distance band,
use the overload that takes a 'visible' parameter but does not have a
'distanceIndex' parameter.  
  
The length of the result array is used to limit the number of spheres checked.
If you provide a result array of length 20, and a firstIndex of 10, then the
query will only examine spheres 10 through 30 to see if they meet the given
visibility and/or distance constraints.

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

