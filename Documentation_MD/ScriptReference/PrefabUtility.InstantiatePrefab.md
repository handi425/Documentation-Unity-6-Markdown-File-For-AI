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

#  [PrefabUtility](PrefabUtility.html).InstantiatePrefab

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

public static Object InstantiatePrefab([Object](Object.html)
assetComponentOrGameObject);

## Declaration

public static Object InstantiatePrefab([Object](Object.html)
assetComponentOrGameObject,
[SceneManagement.Scene](SceneManagement.Scene.html) destinationScene);

### Parameters

assetComponentOrGameObject | Prefab Asset to instantiate.  
---|---  
destinationScene | Scene to instantiate the Prefab in.  
  
### Returns

**Object** The GameObject at the root of the Prefab.

### Description

Instantiates the given Prefab in a given Scene.

This is similar to Instantiate but creates a Prefab connection to the Prefab.
If you do not specify a Scene handle, the Prefab is instantiated in the active
Scene.  
  
**Note:** You should not instantiate Prefabs from the
[OnValidate()](MonoBehaviour.OnValidate.html) or
[Awake()](MonoBehaviour.Awake.html) method. This is because the order in which
GameObjects become awake is not deterministic, and therefore can result in
unexpected behaviour. If you try this, Unity will generate a warning reading
"SendMessage cannot be called during Awake, CheckConsistency, or OnValidate".

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class Example
    {
        [[MenuItem](MenuItem.html)("Examples/Instantiate Selected")]
        static void InstantiatePrefab()
        {
            [Selection.activeObject](Selection-activeObject.html) = [PrefabUtility.InstantiatePrefab](PrefabUtility.InstantiatePrefab.html)([Selection.activeObject](Selection-activeObject.html) as [GameObject](GameObject.html));
        }  
      
        [[MenuItem](MenuItem.html)("Examples/Instantiate Selected", true)]
        static bool ValidateInstantiatePrefab()
        {
            [GameObject](GameObject.html) go = [Selection.activeObject](Selection-activeObject.html) as [GameObject](GameObject.html);
            if (go == null)
                return false;  
      
            return [PrefabUtility.IsPartOfPrefabAsset](PrefabUtility.IsPartOfPrefabAsset.html)(go);
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

