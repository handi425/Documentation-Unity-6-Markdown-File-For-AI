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

#  [PrefabUtility](PrefabUtility.html).RevertRemovedGameObject

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

public static void RevertRemovedGameObject([GameObject](GameObject.html)
gameObjectInInstance, [GameObject](GameObject.html) assetGameObject,
[InteractionMode](InteractionMode.html) action);

### Parameters

gameObjectInInstance | A GameObject in the Prefab instance containing the removed GameObject.  
---|---  
assetGameObject | The GameObject on the Prefab Asset corresponding to the removed GameObject on the instance.  
action | The interaction mode for this action.  
  
### Description

Adds this removed GameObject back on the Prefab instance.

After the revert action the GameObject will once again exist on the Prefab
instance.  
  
The GameObject's components and children will also exist again, unless they
had previously been removed.  
  
Note that added GameObjects and added component overrides, which were in the
hierarchy of the reverted GameObject before it was removed, will not be
restored.  
  
Additional resources:
[PrefabUtility.ApplyRemovedGameObject](PrefabUtility.ApplyRemovedGameObject.html),
[PrefabUtility.GetRemovedGameObjects](PrefabUtility.GetRemovedGameObjects.html).

    
    
    using System.Collections.Generic;
    using System.IO;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.SceneManagement;
    using UnityEngine;  
      
    // Creates new menu items under 'Examples' in the main menu.
    public class RevertRemovedGameObjectExample
    {
        [[MenuItem](MenuItem.html)("Examples/RevertRemovedGameObject Example 1")]
        static void CreatePrefabAndRevertChanges()
        {
            // Create folder Prefabs and set the path as within the Prefabs folder,
            // and name it as the [GameObject](GameObject.html)'s name with the .Prefab format
            if (![Directory.Exists](Windows.Directory.Exists.html)("Assets/Prefabs"))
                [AssetDatabase.CreateFolder](AssetDatabase.CreateFolder.html)("Assets", "Prefabs");  
      
            //Setup hierarchy with root and one child
            [GameObject](GameObject.html) rootGameObject = new [GameObject](GameObject.html)("Root");
            [GameObject](GameObject.html) child = new [GameObject](GameObject.html)("Child");
            child.transform.parent = rootGameObject.transform;  
      
            //Create prefab based on the [GameObject](GameObject.html) hierarchy we just created
            [GameObject](GameObject.html) prefabAsset = [PrefabUtility.SaveAsPrefabAssetAndConnect](PrefabUtility.SaveAsPrefabAssetAndConnect.html)(rootGameObject, "Assets/Prefabs/" + rootGameObject.name + ".prefab", [InteractionMode.AutomatedAction](InteractionMode.AutomatedAction.html));  
      
            //Get the corresponding object matching the Child [GameObject](GameObject.html) that was destroyed
            [GameObject](GameObject.html) correspondingChildGameObject = prefabAsset.transform.GetChild(0).gameObject;  
      
            //Destroy child [GameObject](GameObject.html) so we can apply the override to the Prefab
            [Object.DestroyImmediate](Object.DestroyImmediate.html)(child);  
      
            //Use the variables from above to revert the removed [GameObject](GameObject.html) override in the instance and restore the child [GameObject](GameObject.html)
            [PrefabUtility.RevertRemovedGameObject](PrefabUtility.RevertRemovedGameObject.html)(rootGameObject, correspondingChildGameObject, [InteractionMode.AutomatedAction](InteractionMode.AutomatedAction.html));  
      
            if (prefabAsset.transform.childCount == 1)
                [Debug.Log](Debug.Log.html)("'Child' [GameObject](GameObject.html) was removed and the override reverted successfully.");
            else
                [Debug.Log](Debug.Log.html)("The override was not reverted successfully");
        }  
      
        [[MenuItem](MenuItem.html)("Examples/RevertRemovedGameObject Example 2")]
        static void CreatePrefabAndApplyChangesWithGetRemovedGameObjects()
        {
            // Create folder Prefabs and set the path as within the Prefabs folder,
            // and name it as the [GameObject](GameObject.html)'s name with the .Prefab format
            if (![Directory.Exists](Windows.Directory.Exists.html)("Assets/Prefabs"))
                [AssetDatabase.CreateFolder](AssetDatabase.CreateFolder.html)("Assets", "Prefabs");  
      
            //Setup hierarchy with root and one child
            [GameObject](GameObject.html) rootGameObject = new [GameObject](GameObject.html)("Root");
            [GameObject](GameObject.html) child = new [GameObject](GameObject.html)("Child");
            child.transform.parent = rootGameObject.transform;  
      
            //Create prefab based on the [GameObject](GameObject.html) hierarchy we just created
            [GameObject](GameObject.html) prefabAsset = [PrefabUtility.SaveAsPrefabAssetAndConnect](PrefabUtility.SaveAsPrefabAssetAndConnect.html)(rootGameObject, "Assets/Prefabs/" + rootGameObject.name + ".prefab", [InteractionMode.AutomatedAction](InteractionMode.AutomatedAction.html));  
      
            //Destroy child [GameObject](GameObject.html) so we can apply the override to the Prefab
            [Object.DestroyImmediate](Object.DestroyImmediate.html)(child);  
      
            //Get the override and the information to apply the changes to the Prefab asset
            List<[RemovedGameObject](SceneManagement.RemovedGameObject.html)> removedGameObjects = [PrefabUtility.GetRemovedGameObjects](PrefabUtility.GetRemovedGameObjects.html)(rootGameObject);
            [GameObject](GameObject.html) assetGameObject = removedGameObjects[0].assetGameObject;
            [GameObject](GameObject.html) parentOfRemovedGameObjectInInstance = removedGameObjects[0].parentOfRemovedGameObjectInInstance;  
      
            //Use the variables from above to revert the removed [GameObject](GameObject.html) override in the instance and restore the child [GameObject](GameObject.html)
            [PrefabUtility.RevertRemovedGameObject](PrefabUtility.RevertRemovedGameObject.html)(parentOfRemovedGameObjectInInstance, assetGameObject, [InteractionMode.AutomatedAction](InteractionMode.AutomatedAction.html));  
      
            if (prefabAsset.transform.childCount == 1)
                [Debug.Log](Debug.Log.html)("'Child' [GameObject](GameObject.html) was removed and the override reverted successfully.");
            else
                [Debug.Log](Debug.Log.html)("The override was not reverted successfully");
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

