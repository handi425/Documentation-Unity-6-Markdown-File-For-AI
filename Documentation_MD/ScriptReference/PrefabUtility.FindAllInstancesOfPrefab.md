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

#  [PrefabUtility](PrefabUtility.html).FindAllInstancesOfPrefab

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

public static GameObject[]
FindAllInstancesOfPrefab([GameObject](GameObject.html) prefabRoot);

## Declaration

public static GameObject[]
FindAllInstancesOfPrefab([GameObject](GameObject.html) prefabRoot,
[SceneManagement.Scene](SceneManagement.Scene.html) scene);

### Parameters

prefabRoot | The root GameObject of a Prefab asset.  
---|---  
scene | The scene to search for Prefab instances. The scene you specify must be valid and loaded.  
  
### Returns

**GameObject[]** The root GameObjects for all instances of the Prefab asset
with root `prefabRoot`.

### Description

Retrieves the root GameObjects for all instances of the Prefab asset with root
`prefabRoot` found in all currently loaded scenes. If `prefabRoot` is not a
valid Prefab asset root GameObject, an `ArgumentException` is thrown.

FindAllInstancesOfPrefab will not return nested Prefab instances.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using UnityEngine.SceneManagement;
    using NUnit.Framework;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        public [GameObject](GameObject.html) prefabAssetRoot;
        private void Start()
        {
            var expectedInstance = ([GameObject](GameObject.html))[PrefabUtility.InstantiatePrefab](PrefabUtility.InstantiatePrefab.html)(prefabAssetRoot);
            var instances = [PrefabUtility.FindAllInstancesOfPrefab](PrefabUtility.FindAllInstancesOfPrefab.html)(prefabAssetRoot);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(1, instances.Length);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(expectedInstance, instances[0]);
        }
    }
    

* * *

### Description

Returns the root GameObjects for all instances of the Prefab asset with root
`prefabRoot` found in `scene`. If `prefabRoot` is not a valid Prefab asset
root GameObject, or `scene` is not valid and loaded, `ArgumentException` is
thrown.

FindAllInstancesOfPrefab will not return nested Prefab instances.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using UnityEngine.SceneManagement;
    using NUnit.Framework;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        public [GameObject](GameObject.html) prefabAssetRoot;
        private void Start()
        {
            var expectedInstance = ([GameObject](GameObject.html))[PrefabUtility.InstantiatePrefab](PrefabUtility.InstantiatePrefab.html)(prefabAssetRoot);
            var instances = [PrefabUtility.FindAllInstancesOfPrefab](PrefabUtility.FindAllInstancesOfPrefab.html)(prefabAssetRoot, [SceneManager.GetActiveScene](SceneManagement.SceneManager.GetActiveScene.html)());
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(1, instances.Length);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(expectedInstance, instances[0]);
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

