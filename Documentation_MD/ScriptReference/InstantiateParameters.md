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

# InstantiateParameters

struct in UnityEngine

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

Parameters for Object.Instantiate and Object.InstantiateAsync.

This structure is used in [Object.Instantiate](Object.Instantiate.html) and
[Object.InstantiateAsync](Object.InstantiateAsync.html) in order to provide
maximum flexibility in the parameters you provide. It has the added benefit of
unifying the meaning of the parameters in both methods.  
  
The behaviour of the different parameter combinations is:

  * **Default** : The instance will have the same local position and rotation as the original, it won't have a parent and it will be in the active scene.
  * `worldSpace`: The instance will have the same world position and rotation as the original.
  * **Default, method takes position and rotation** : Sets those values to the transform of the instance in local space.
  * `worldSpace` **, method takes position and rotation** : Sets those values to the transform of the instance in world space.
  * `parent`: The instance will be a child of `parent` and will have the same local position and rotation as the original.
  * `parent` **and** `worldSpace`: The instance will be a child of `parent` and will have the same world position and rotation as the original.
  * `parent` **, method takes position and rotation** : The instance will be a child of `parent` and the values will be set as local.
  * `parent` **and** `worldSpace`**, method takes position and rotation** : The instance will be a child of `parent` and the values will be set as world space.
  * `scene` **and any combination of position, rotation and** `worldSpace`: The same behaviour as that combination, but the instance will be in `scene`.
  * `scene` **and** `parent`: `scene` will be ignored because child objects are always in the same scene as the `parent`.

### Properties

[parent](InstantiateParameters-parent.html)| The desired parent.  
---|---  
[scene](InstantiateParameters-scene.html)| The desired scene.  
[worldSpace](InstantiateParameters-worldSpace.html)| Choose between world
space or local space.  
  
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

