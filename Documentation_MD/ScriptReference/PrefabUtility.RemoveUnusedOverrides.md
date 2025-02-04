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

#  [PrefabUtility](PrefabUtility.html).RemoveUnusedOverrides

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

public static void RemoveUnusedOverrides(GameObject[] prefabInstances,
[InteractionMode](InteractionMode.html) action);

### Parameters

prefabInstances | List of Prefab instances to remove unused overrides from.  
---|---  
action | UserAction will record undo and write result to Editor log file.  
  
### Description

This method identifies and removes all unused overrides from a list of Prefab
Instance roots. See the manual [Unused
Overides](https://docs.unity3d.com/2023.1/Documentation/Manual/UnusedOverrides.html)
for more detail.

    
    
    using System.IO;
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class RemoveUnusedOverridesExample
    {
        // Creates a new menu item 'Examples > Remove Unused Overrides Example' in the main menu.
        [[MenuItem](MenuItem.html)("Examples/Remove Unused Overrides Example")]
        static void RemoveUnusedOverrides()
        {
            var exampleGameObject = new [GameObject](GameObject.html)("Example", typeof([BoxCollider](BoxCollider.html)));  
      
            // Create folder Prefabs and set the path as within the Prefabs folder,
            // and name it as the [GameObject](GameObject.html)'s name with the .Prefab format
            if (![Directory.Exists](Windows.Directory.Exists.html)("Assets/Prefabs"))
                [AssetDatabase.CreateFolder](AssetDatabase.CreateFolder.html)("Assets", "Prefabs");
            string localPath = "Assets/Prefabs/" + exampleGameObject.name + ".prefab";  
      
            // Make sure the file name is unique, in case an existing Prefab has the same name.
            localPath = [AssetDatabase.GenerateUniqueAssetPath](AssetDatabase.GenerateUniqueAssetPath.html)(localPath);  
      
            // Create the new Prefab and log whether Prefab was saved successfully.
            var prefabAsset = [PrefabUtility.SaveAsPrefabAssetAndConnect](PrefabUtility.SaveAsPrefabAssetAndConnect.html)(exampleGameObject, localPath, [InteractionMode.UserAction](InteractionMode.UserAction.html), out bool prefabSuccess);  
      
            //Set a value on the example script and record it
            exampleGameObject.GetComponent<[BoxCollider](BoxCollider.html)>().center = new [Vector3](Vector3.html)(2.0f, 2.0f, 2.0f);
            [PrefabUtility.RecordPrefabInstancePropertyModifications](PrefabUtility.RecordPrefabInstancePropertyModifications.html)(exampleGameObject.GetComponent<[BoxCollider](BoxCollider.html)>());  
      
            //Remove the component from the prefab asset. We now have an unused override.
            [PrefabUtility.ApplyRemovedComponent](PrefabUtility.ApplyRemovedComponent.html)(exampleGameObject, prefabAsset.GetComponent(typeof([BoxCollider](BoxCollider.html))), [InteractionMode.UserAction](InteractionMode.UserAction.html));  
      
            //Remove the unused override that was created earlier
            [PrefabUtility.RemoveUnusedOverrides](PrefabUtility.RemoveUnusedOverrides.html)(new [] { exampleGameObject }, [InteractionMode.UserAction](InteractionMode.UserAction.html));
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

