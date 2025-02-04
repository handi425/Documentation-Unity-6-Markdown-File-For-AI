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

#  [HideFlags](HideFlags.html).DontSave

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

The object will not be saved to the Scene. **It will not be destroyed when a new Scene is loaded**. It is a shortcut for HideFlags.DontSaveInBuild | HideFlags.DontSaveInEditor | HideFlags.DontUnloadUnusedAsset.

You must manually clear the object from memory using DestroyImmediate to avoid
memory leaks.  
  
For Prefab instances in a scene, you can set the hideflag on the Prefab
instance handle object as a way to set the same hideflags on all the objects
of the Prefab instance. (See
[PrefabUtility.GetPrefabInstanceHandle](PrefabUtility.GetPrefabInstanceHandle.html)).

    
    
    using System.IO;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.SceneManagement;
    using UnityEngine;  
      
    // Creates new menu items under 'Examples' in the main menu.
    public class DontSaveExamples
    {
        [[MenuItem](MenuItem.html)("Examples/[GameObject](GameObject.html) (and child) [HideFlags.DontSave](HideFlags.DontSave.html) example")]
        static void DontSaveExample_RootWithDontSave()
        {
            //Setup hierarchy with root and one child
            [GameObject](GameObject.html) rootGameObject = new [GameObject](GameObject.html)("Root");
            [GameObject](GameObject.html) child = new [GameObject](GameObject.html)("Child");
            child.transform.parent = rootGameObject.transform;  
      
            rootGameObject.hideFlags = [HideFlags.DontSave](HideFlags.DontSave.html);
            //child.hideFlags = [HideFlags.DontSave](HideFlags.DontSave.html); //No difference for plain GameObjects as the root is marked with DontSave  
      
            //Load new scene
            [EditorSceneManager.NewScene](SceneManagement.EditorSceneManager.NewScene.html)([NewSceneSetup.EmptyScene](SceneManagement.NewSceneSetup.EmptyScene.html), [NewSceneMode.Single](SceneManagement.NewSceneMode.Single.html));  
      
            //Both objects still exist as the root is marked with DontSave
            [Debug.Log](Debug.Log.html)("Root name: " + rootGameObject.name + ", Child name: " + child.name);  
      
            //Remember to clean up, this also deleted the child [GameObject](GameObject.html)
            [Object.DestroyImmediate](Object.DestroyImmediate.html)(rootGameObject);
        }  
      
        [[MenuItem](MenuItem.html)("Examples/Save Prefab with child [HideFlags.DontSave](HideFlags.DontSave.html) example")]
        static void DontSaveExample_Prefab_ChildNotSavedToDisk()
        {
            //Ensure the existence of a Prefabs folder inside the Assets folder
            if (![Directory.Exists](Windows.Directory.Exists.html)("Assets/Prefabs"))
                [AssetDatabase.CreateFolder](AssetDatabase.CreateFolder.html)("Assets", "Prefabs");  
      
            //Setup hierarchy with root and one child
            [GameObject](GameObject.html) rootGameObject = new [GameObject](GameObject.html)("Root");
            [GameObject](GameObject.html) child = new [GameObject](GameObject.html)("Child");
            child.transform.parent = rootGameObject.transform;  
      
            //Mark child to prevent saving it
            child.hideFlags = [HideFlags.DontSave](HideFlags.DontSave.html);  
      
            //Save the Prefab asset
            [GameObject](GameObject.html) prefabAsset = [PrefabUtility.SaveAsPrefabAsset](PrefabUtility.SaveAsPrefabAsset.html)(rootGameObject, "Assets/Prefabs/Root.prefab");  
      
            //No children in prefab as the child was marked as DontSave. The childCount is 0.
            [Debug.Log](Debug.Log.html)("Child [GameObject](GameObject.html) in Prefab: " + prefabAsset.transform.childCount);  
      
            //Child still exists in scene. The childCount is 1.
            [Debug.Log](Debug.Log.html)("Child [GameObject](GameObject.html) in [Scene](SceneManagement.Scene.html) [GameObject](GameObject.html): " + rootGameObject.transform.childCount);  
      
            //Load new scene
            [EditorSceneManager.NewScene](SceneManagement.EditorSceneManager.NewScene.html)([NewSceneSetup.EmptyScene](SceneManagement.NewSceneSetup.EmptyScene.html), [NewSceneMode.Single](SceneManagement.NewSceneMode.Single.html));  
      
            //Child is deleted as it was a child of the root [GameObject](GameObject.html) that got deleted in the scene transition
            if (child == null)
                [Debug.Log](Debug.Log.html)("Child deleted correctly");
            else
                [Debug.Log](Debug.Log.html)("Child was not deleted successfully");
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

