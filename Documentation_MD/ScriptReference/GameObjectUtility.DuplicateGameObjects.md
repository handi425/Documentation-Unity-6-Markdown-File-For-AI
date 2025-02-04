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

#  [GameObjectUtility](GameObjectUtility.html).DuplicateGameObjects

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

public static GameObject[] DuplicateGameObjects(GameObject[] gameObjects);

### Parameters

gameObjects | The array of GameObjects to be duplicated.  
---|---  
  
### Returns

**GameObject[]** The array of the duplicated GameObject roots.

### Description

Duplicates an array of GameObjects and returns the array of the new GameObject
roots.

Duplicates GameObjects within a Scene. Each GameObject will be on the same
level in the hierarchy as its original GameObject, and they will share the
same parent. If there are any children or components that belong to the
original GameObject, the duplicate will have them as well. If a parent and a
child are both added to the input array, only the parent will be duplicated
and returned (similar to the way Ctrl + D works in the editor).  
  
For duplicating a single GameObject use
[DuplicateGameObject](GameObjectUtility.DuplicateGameObject.html). For
duplicating Assets use
[AssetDatabase.CopyAsset](AssetDatabase.CopyAsset.html).

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public static class DuplicateGameObjectsExample
    {
        // Create context menu
        [[MenuItem](MenuItem.html)("Example/Duplicating GameObjects Example")]
        public static void DuplicatingGameObjectsExample()
        {
            // Creating the original GameObjects
            [GameObject](GameObject.html) gameObject1 = new [GameObject](GameObject.html)("gameObject1");
            [GameObject](GameObject.html) gameObject2 = new [GameObject](GameObject.html)("gameObject2");
            [GameObject](GameObject.html) gameObject3 = new [GameObject](GameObject.html)("gameObject3");  
      
            // Creating an array of all GameObjects
            [GameObject](GameObject.html)[] gameObjectArray = { gameObject1, gameObject2, gameObject3 };  
      
            // Duplicating the array of GameObjects
            [GameObject](GameObject.html)[] duplicatedGameObjectArray = [GameObjectUtility.DuplicateGameObjects](GameObjectUtility.DuplicateGameObjects.html)(gameObjectArray);  
      
            // [Display](Display.html) the names of the duplicated GameObjects in the console
            [Debug.Log](Debug.Log.html)("Duplicated GameObjects: ");
            for (int i = 0; i < duplicatedGameObjectArray.Length; i++)
            {
                [Debug.Log](Debug.Log.html)(duplicatedGameObjectArray[i].name);
            }
        }  
      
        // Create context menu
        [[MenuItem](MenuItem.html)("Example/Duplicating [Hierarchy](Unity.Hierarchy.Hierarchy.html) Example")]
        public static void DuplicatingHierarchyExample()
        {
            // Creating the original GameObjects
            [GameObject](GameObject.html) parent = new [GameObject](GameObject.html)("parent");
            [GameObject](GameObject.html) child1 = new [GameObject](GameObject.html)("child1");
            [GameObject](GameObject.html) child2 = new [GameObject](GameObject.html)("child2");  
      
            // Assigning parents to children
            child1.transform.parent = parent.transform;
            child2.transform.parent = parent.transform;  
      
            // Creating an array of all GameObjects
            [GameObject](GameObject.html)[] gameObjectArray = { parent, child1, child2 };  
      
            // Duplicating the array of GameObjects
            [GameObject](GameObject.html)[] duplicatedGameObjectArray = [GameObjectUtility.DuplicateGameObjects](GameObjectUtility.DuplicateGameObjects.html)(gameObjectArray);  
      
            // [Display](Display.html) the names of the duplicated GameObjects in the console
            // Only the parent will be returned
            [Debug.Log](Debug.Log.html)("Duplicated GameObjects: ");
            for (int i = 0; i < duplicatedGameObjectArray.Length; i++)
            {
                [Debug.Log](Debug.Log.html)(duplicatedGameObjectArray[i].name);
            }
        }
    }
    

Any errors and warnings from the duplication operation are reported in the log
and the console.

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

