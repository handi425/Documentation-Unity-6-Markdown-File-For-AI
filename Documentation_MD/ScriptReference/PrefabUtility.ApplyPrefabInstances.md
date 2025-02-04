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

#  [PrefabUtility](PrefabUtility.html).ApplyPrefabInstances

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

public static void ApplyPrefabInstances(GameObject[] instanceRoots,
[InteractionMode](InteractionMode.html) action);

### Parameters

instanceRoots | The roots of the given Prefab instances.  
---|---  
action | The interaction mode for this action.  
  
### Description

Applies all overrides from a list of Prefab instances to their Prefab Assets.

This method allows you to apply the complete modified state of Prefab
instances to their source Prefab Assets, which includes all property
overrides, added and removed components, and added child GameObjects
(including added child Prefab instances).  
  
It mirrors the functionality of the "Apply All" button in the [overrides
menu](../Manual/EditingPrefabViaInstance.html) in the editor. To use this
method, you must first modify an existing Prefab instance in some way, such as
modifying properties, or adding or removing GameObjects or components.  
  
Modifications to a Prefab instance that have not been applied are called
[instance overrides](../Manual/PrefabInstanceOverrides.html). The act of
applying the modifications means the modifications become part of the Prefab
Asset, and are no longer overrides.  
  
When applying all modifications to a Prefab Asset using this method to nested
Prefabs or Prefab variants, the changes are always applied to the outermost
Prefab. To apply changes to inner Prefabs, you can use the other methods such
as
[PrefabUtility.ApplyAddedComponent](PrefabUtility.ApplyAddedComponent.html),
[PrefabUtility.ApplyAddedGameObject](PrefabUtility.ApplyAddedGameObject.html),
[PrefabUtility.ApplyRemovedComponent](PrefabUtility.ApplyRemovedComponent.html),
[PrefabUtility.ApplyRemovedGameObject](PrefabUtility.ApplyRemovedGameObject.html)
and
[PrefabUtility.ApplyObjectOverride](PrefabUtility.ApplyObjectOverride.html).  
  
The Transform position and rotation of a root GameObject in a Prefab instance
cannot be applied, nor can other [default
override](PrefabUtility.IsDefaultOverride.html) properties.  
  
You can read more in the user manual about [modifying and applying changes to
Prefab instances](../Manual/EditingPrefabViaInstance.html).  
  
Additional resources:
[PrefabUtility.ApplyPrefabInstance](PrefabUtility.ApplyPrefabInstance.html),
[PrefabUtility.ApplyAddedComponent](PrefabUtility.ApplyAddedComponent.html),
[PrefabUtility.ApplyAddedGameObject](PrefabUtility.ApplyAddedGameObject.html),
[PrefabUtility.ApplyObjectOverride](PrefabUtility.ApplyObjectOverride.html),
[PrefabUtility.ApplyPropertyOverride](PrefabUtility.ApplyPropertyOverride.html),
[PrefabUtility.ApplyRemovedComponent](PrefabUtility.ApplyRemovedComponent.html),
[PrefabUtility.ApplyRemovedGameObject](PrefabUtility.ApplyRemovedGameObject.html).

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

