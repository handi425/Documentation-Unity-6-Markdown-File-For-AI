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

#  [PrefabUtility](PrefabUtility.html).ReplacePrefabAssetOfPrefabInstance

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

public static void
ReplacePrefabAssetOfPrefabInstance([GameObject](GameObject.html)
prefabInstanceRoot, [GameObject](GameObject.html) prefabAssetRoot,
[InteractionMode](InteractionMode.html) mode);

## Declaration

public static void
ReplacePrefabAssetOfPrefabInstance([GameObject](GameObject.html)
prefabInstanceRoot, [GameObject](GameObject.html) prefabAssetRoot,
[PrefabReplacingSettings](PrefabReplacingSettings.html) settings,
[InteractionMode](InteractionMode.html) mode);

### Parameters

prefabInstanceRoot | The Prefab instance root that will have its Prefab Asset replaced.  
---|---  
prefabAssetRoot | The new Prefab Asset used for the Prefab instance.  
mode | The interaction mode used.  
settings | The settings used to control the details of the replacement.  
  
### Description

Replace the Prefab Asset for a Prefab instance that exists in a Scene or for a
nested Prefab instance inside another Prefab.

This function will keep the Prefab instance root position, rotation and scale
in the Scene but merge the contents from the new Prefab Asset while, by
default, maintaining as many overrides and references as possible by using
name based matching. Note that the root GameObject and its components will
always reuse these objects regardless of the
[ObjectMatchMode](ObjectMatchMode.html), so references to these objects will
always survive a replacement. Use
[ObjectMatchMode.ByHierarchy](ObjectMatchMode.ByHierarchy.html) which will
retain references if GameObjects and Components are matched up using their
full GameObject hierarchy path so ensure all siblings have unique names. When
using [ObjectMatchMode.ByName](ObjectMatchMode.ByName.html) an object match is
only performed if the name match is unique. It is therefore recommended that
the Prefab instance and Prefab Asset only have unique names in the hierarchy
of GameObjects. Matching cannot be done for GameObjects with duplicate names.  
  
No property overrides are deleted from the serialized state of the Prefab
instance so replacing back and forth between different Prefab Assets is a non-
destructive action for property overrides. When the final Prefab instance is
decided upon then any unused overrides can be cleaned up from either Hierarchy
or Overrides window. Added Components are preserved if a name match exists,
otherwise the added Component is deleted. Added GameObjects are preserved by
adding them to the root of the new instance if no name match was found for its
parent GameObject. Since an added GameObject can have a full hierarchy under
it, we leave it to you to decide whether it makes sense to delete the object
if it proves redundant on the new instance. This can be done from either the
Hierarchy or Overrides window. For explict control over which overrides should
be cleared use the
[PrefabReplacingSettings.prefabOverridesOptions](PrefabReplacingSettings-
prefabOverridesOptions.html) flags found in the
[PrefabReplacingSettings](PrefabReplacingSettings.html).  
  
Additional resources:
[ReplacePrefabAssetOfPrefabInstances](PrefabUtility.ReplacePrefabAssetOfPrefabInstances.html),
[ConvertToPrefabInstance](PrefabUtility.ConvertToPrefabInstance.html).

    
    
    using System.Collections.Generic;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    class PrefabReplacing
    {
        [[MenuItem](MenuItem.html)("Assets/Replace [Scene](SceneManagement.Scene.html) [Selection](Selection.html) with Prefab [Asset](VersionControl.Asset.html)", false, 32)]
        static void ReplaceSelectedWithPrefabInstance([MenuCommand](MenuCommand.html) menuCommand)
        {
            [GameObject](GameObject.html) prefabAsset = null;
            var listOfInstanceRoots = new List<[GameObject](GameObject.html)>();
            var listOfPlainGameObjects = new List<[GameObject](GameObject.html)>();
            foreach (var go in [Selection.gameObjects](Selection-gameObjects.html))
            {
                if ([AssetDatabase.Contains](AssetDatabase.Contains.html)(go))
                    prefabAsset = go;
                else if ([PrefabUtility.IsOutermostPrefabInstanceRoot](PrefabUtility.IsOutermostPrefabInstanceRoot.html)(go))
                    listOfInstanceRoots.Add(go);
                else if (![PrefabUtility.IsPartOfNonAssetPrefabInstance](PrefabUtility.IsPartOfNonAssetPrefabInstance.html)(go))
                    listOfPlainGameObjects.Add(go);
            }  
      
            if (prefabAsset == null || (listOfInstanceRoots.Count == 0 && listOfPlainGameObjects.Count == 0))
            {
                ShowHelpDialog(prefabAsset);
                return;
            }  
      
            if (listOfInstanceRoots.Count > 0)
            {
                var settings = new [PrefabReplacingSettings](PrefabReplacingSettings.html)
                {
                    logInfo = true,
                    objectMatchMode = [ObjectMatchMode.ByHierarchy](ObjectMatchMode.ByHierarchy.html),
                    prefabOverridesOptions = [PrefabOverridesOptions.ClearAllNonDefaultOverrides](PrefabOverridesOptions.ClearAllNonDefaultOverrides.html)
                };
                [PrefabUtility.ReplacePrefabAssetOfPrefabInstances](PrefabUtility.ReplacePrefabAssetOfPrefabInstances.html)(listOfInstanceRoots.ToArray(), prefabAsset, settings, [InteractionMode.UserAction](InteractionMode.UserAction.html));
            }  
      
            if (listOfPlainGameObjects.Count > 0)
            {
                var settings = new [ConvertToPrefabInstanceSettings](ConvertToPrefabInstanceSettings.html)
                {
                    logInfo = true,
                    objectMatchMode = [ObjectMatchMode.ByHierarchy](ObjectMatchMode.ByHierarchy.html),
                };
                [PrefabUtility.ConvertToPrefabInstances](PrefabUtility.ConvertToPrefabInstances.html)(listOfPlainGameObjects.ToArray(), prefabAsset, settings, [InteractionMode.UserAction](InteractionMode.UserAction.html));
            }
        }  
      
        [[MenuItem](MenuItem.html)("Assets/Replace [Scene](SceneManagement.Scene.html) [Selection](Selection.html) with Prefab [Asset](VersionControl.Asset.html)", true, 32)]
        static bool ValidateReplaceSelectedWithPrefabInstance([MenuCommand](MenuCommand.html) menuCommand)
        {
            foreach (var go in [Selection.gameObjects](Selection-gameObjects.html))
            {
                if ([AssetDatabase.Contains](AssetDatabase.Contains.html)(go))
                    return true;
            }  
      
            return false;
        }  
      
        static void ShowHelpDialog([GameObject](GameObject.html) prefabAsset)
        {
            var helptext = "Please make a multiselection with at least one Prefab instance root or plain [GameObject](GameObject.html) in the [Scene](SceneManagement.Scene.html) and one Prefab [Asset](VersionControl.Asset.html) from the Project Browser. \n\nUse Ctrl/Cmd + Click.";
            [EditorUtility.DisplayDialog](EditorUtility.DisplayDialog.html)("Replace Prefab [Asset](VersionControl.Asset.html) of Prefab instance", (prefabAsset == null ? "Prefab [Asset](VersionControl.Asset.html) missing.\n\n" : "Prefab instance missing.\n\n") + helptext, "OK");
        }
    }
    

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

