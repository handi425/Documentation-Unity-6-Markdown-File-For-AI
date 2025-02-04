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

# ClothSkinningCoefficient

struct in UnityEngine

/

Implemented in:[UnityEngine.ClothModule](UnityEngine.ClothModule.html)

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

The ClothSkinningCoefficient struct is used to set up how a
[Cloth](Cloth.html) component is allowed to move with respect to the
[SkinnedMeshRenderer](SkinnedMeshRenderer.html) it is attached to.

This is set using the [Cloth.coefficients](Cloth-coefficients.html) property
on the Cloth component, which is a per-vertex array of
ClothSkinningCoefficient structs. Typically, you will not set these values
from code, but instead, set them up in the editor which shows up when you look
at the Cloth component in the inspector.

### Properties

[collisionSphereDistance](ClothSkinningCoefficient-
collisionSphereDistance.html)| Definition of a sphere a vertex is not allowed
to enter. This allows collision against the animated cloth.  
---|---  
[maxDistance](ClothSkinningCoefficient-maxDistance.html)| Distance a vertex is
allowed to travel from the skinned mesh vertex position.  
  
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

