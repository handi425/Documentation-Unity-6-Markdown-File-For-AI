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

#  [PrefabUtility](PrefabUtility.html).UnpackPrefabInstance

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

public static void UnpackPrefabInstance([GameObject](GameObject.html)
instanceRoot, [PrefabUnpackMode](PrefabUnpackMode.html) unpackMode,
[InteractionMode](InteractionMode.html) action);

### Parameters

instanceRoot | The root of the Prefab instance to unpack.  
---|---  
unpackMode | Whether to unpack the outermost root or unpack completely.  
action | The interaction mode to use for this action.  
  
### Description

Unpacks a given Prefab instance so that it is replaced with the contents of
the Prefab Asset while retaining all override values.

The given object must be the root of a Prefab instance.  
  
The contents of a Prefab Asset is the objects you see when you open it in
Prefab Mode. Unpacking with a PrefabUnpackMode of OutermostRoot will replace
the Prefab instance with that content. Unpacking with a PrefabUnpackMode of
Completely will furthermore also unpack any Prefab instances that are part of
the unpacked content, so that the end result is nothing but regular
GameObjects and no Prefab instances.  
  
The contents of a regular Prefab or a Model Prefab always has a regular
GameObject at the root, so unpacking one of those will leave a regular
GameObject at the root where the Prefab instance was before.  
  
The contents of a Prefab Variant has an instance of the base Prefab at the
root, so unpacking a Prefab Variant with a PrefabUnpackMode of OutermostRoot
will leave an instance of the base Prefab where the Prefab Variant instance
was before.  
  
Unpacking throws an ArgumentException if the given object is not the root of a
Prefab instance, or if it’s part of a Prefab Asset. This does not include
Prefab contents opened in Prefab Mode.  
  
InteractionMode determines if the action should be undoable.

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

