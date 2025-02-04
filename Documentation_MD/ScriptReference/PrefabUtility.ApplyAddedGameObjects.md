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

#  [PrefabUtility](PrefabUtility.html).ApplyAddedGameObjects

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

public static void ApplyAddedGameObjects(GameObject[] gameObjects, string
assetPath, [InteractionMode](InteractionMode.html) action);

### Parameters

gameObjects | The added GameObjects on the Prefab instance to apply.  
---|---  
assetPath | The path of the Prefab Asset to apply to.  
action | The interaction mode for this action.  
  
### Description

Applies the added GameObjects to the Prefab Asset at the given asset path.

This method allows you to apply added GameObjects to an existing Prefab. It
mirrors the functionality in the editor, described in [the user manual
here](../Manual/PrefabOverridesMultiLevel.html). To use this method, you must
first add the GameObjects to an existing Prefab instance.  
  
An added GameObject is a type of [Instance
Override](../Manual/PrefabInstanceOverrides.html). The act of applying added
GameObjects to the Prefab means they will become part of the Prefab Asset, and
will no longer be overrides on the Prefab instance.  
  
When applying added GameObjects to a Prefab Asset, you must supply the asset
path as a parameter. This is because there are some situations where there are
multiple possible targets to apply the change to. For example, if added
GameObjects have been added to a GameObject that is part of a [nested
Prefab](../Manual/NestedPrefabs.html), you may have the choice of applying the
changes to the inner nested Prefab Asset, or to the outer root Prefab Asset.
Therefore, by specifying the asset path, you make it clear to Unity which
Prefab Asset the change must be applied to.  
  
You can read more in the user manual about the [choice of apply
targets](../Manual/PrefabOverridesMultiLevel.html).  
  
Additional resources:
[PrefabUtility.ApplyAddedGameObject](PrefabUtility.ApplyAddedGameObject.html),
[PrefabUtility.ApplyAddedComponent](PrefabUtility.ApplyAddedComponent.html),
[PrefabUtility.ApplyObjectOverride](PrefabUtility.ApplyObjectOverride.html),
[PrefabUtility.ApplyPropertyOverride](PrefabUtility.ApplyPropertyOverride.html),
[PrefabUtility.ApplyRemovedComponent](PrefabUtility.ApplyRemovedComponent.html),
[PrefabUtility.ApplyPrefabInstance](PrefabUtility.ApplyPrefabInstance.html).

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

