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

#  [Resources](Resources.html).FindObjectsOfTypeAll

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

public static T[] FindObjectsOfTypeAll();

### Description

Returns a list of all objects of Type `T`.

This function can return any type of Unity object that is loaded, including
game objects, prefabs, materials, meshes, textures, etc. It will also list
internal objects, therefore be careful with the way you handle the returned
objects.  
  
Contrary to Object.FindObjectsOfType this function will also list disabled
objects.

    
    
    using System.Collections.Generic;
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        List<[GameObject](GameObject.html)> GetAllObjectsOnlyInScene()
        {
            List<[GameObject](GameObject.html)> objectsInScene = new List<[GameObject](GameObject.html)>();  
      
            foreach ([GameObject](GameObject.html) go in [Resources.FindObjectsOfTypeAll](Resources.FindObjectsOfTypeAll.html)(typeof([GameObject](GameObject.html))) as [GameObject](GameObject.html)[])
            {
                if (![EditorUtility.IsPersistent](EditorUtility.IsPersistent.html)(go.transform.root.gameObject) && !(go.hideFlags == [HideFlags.NotEditable](HideFlags.NotEditable.html) || go.hideFlags == [HideFlags.HideAndDontSave](HideFlags.HideAndDontSave.html)))
                    objectsInScene.Add(go);
            }  
      
            return objectsInScene;
        }
    }
    

This will return all GameObjects in the scene, in List<GameObject> format.

    
    
    using System.Collections.Generic;
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        List<[GameObject](GameObject.html)> GetNonSceneObjects()
        {
            List<[GameObject](GameObject.html)> objectsInScene = new List<[GameObject](GameObject.html)>();  
      
            foreach ([GameObject](GameObject.html) go in [Resources.FindObjectsOfTypeAll](Resources.FindObjectsOfTypeAll.html)(typeof([GameObject](GameObject.html))) as [GameObject](GameObject.html)[])
            {
                if ([EditorUtility.IsPersistent](EditorUtility.IsPersistent.html)(go.transform.root.gameObject) && !(go.hideFlags == [HideFlags.NotEditable](HideFlags.NotEditable.html) || go.hideFlags == [HideFlags.HideAndDontSave](HideFlags.HideAndDontSave.html)))
                    objectsInScene.Add(go);
            }  
      
            return objectsInScene;
        }
    }
    

This will return all GameObjects that are also Prefabs in the Resources
folder.

* * *

## Declaration

public static Object[] FindObjectsOfTypeAll(Type type);

### Description

Returns a list of all objects of Type `type`.

This function using non-generic types can return any type of Unity object that
is loaded, including game objects, prefabs, materials, meshes, textures, etc.
It will also list internal stuff, therefore be careful the way you handle the
returned objects. Contrary to
[Object.FindObjectsOfType](Object.FindObjectsOfType.html) this function will
also list disabled objects.  
  
Note: that this function is very slow and is not recommended to be used every
frame.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using System.Collections.Generic;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        List<UnityEngine.Object> GetSceneObjectsNonGeneric()
        {
            List<UnityEngine.Object> objectsInScene = new List<UnityEngine.Object>();  
      
            foreach (UnityEngine.Object go in [Resources.FindObjectsOfTypeAll](Resources.FindObjectsOfTypeAll.html)(typeof(UnityEngine.Object)) as UnityEngine.Object[])
            {
                [GameObject](GameObject.html) cGO = go as [GameObject](GameObject.html);
                if (cGO != null && ![EditorUtility.IsPersistent](EditorUtility.IsPersistent.html)(cGO.transform.root.gameObject) && !(go.hideFlags == [HideFlags.NotEditable](HideFlags.NotEditable.html) || go.hideFlags == [HideFlags.HideAndDontSave](HideFlags.HideAndDontSave.html)))
                    objectsInScene.Add(go);
            }  
      
            return objectsInScene;
        }
    }
    

Find all gameObjects in scene using non-generic methods.

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

