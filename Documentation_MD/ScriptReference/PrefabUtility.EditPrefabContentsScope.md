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

# EditPrefabContentsScope

struct in UnityEditor

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

Disposable helper struct for automatically loading the contents of a Prefab
file, saving the contents and unloading the contents again.

This struct allows you to temporarily load the GameObject contents of a Prefab
file, modify the contents to your liking inside of a block of code and
automatically save the result back to the Prefab file as well as unload the
temporary contents when the scope is exited.  
  
This scope struct wraps the API’s
[LoadPrefabContents](PrefabUtility.LoadPrefabContents.html),
[SaveAsPrefabAsset](PrefabUtility.SaveAsPrefabAsset.html) and
[UnloadPrefabContents](PrefabUtility.UnloadPrefabContents.html).

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public static class PrefabUtilityTesting
    {
        [[MenuItem](MenuItem.html)("Prefabs/Test_EditPrefabContentsScope")]
        public static void Test()
        {
            // Create a simple test Prefab [Asset](VersionControl.Asset.html). Looks like this:
            // Root
            //    A
            //    B
            //    C
            var assetPath = "Assets/MyTempPrefab.prefab";
            var source = new [GameObject](GameObject.html)("Root");
            var childA = new [GameObject](GameObject.html)("A");
            var childB = new [GameObject](GameObject.html)("B");
            var childC = new [GameObject](GameObject.html)("C");
            childA.transform.parent = source.transform;
            childB.transform.parent = source.transform;
            childC.transform.parent = source.transform;
            [PrefabUtility.SaveAsPrefabAsset](PrefabUtility.SaveAsPrefabAsset.html)(source, assetPath);  
      
            using (var editingScope = new [PrefabUtility.EditPrefabContentsScope](PrefabUtility.EditPrefabContentsScope.html)(assetPath))
            {
                var prefabRoot = editingScope.prefabContentsRoot;  
      
                // Removing GameObjects is supported
                [Object.DestroyImmediate](Object.DestroyImmediate.html)(prefabRoot.transform.GetChild(2).gameObject);  
      
                // Reordering and reparenting are supported
                prefabRoot.transform.GetChild(1).parent = prefabRoot.transform.GetChild(0);  
      
                // Adding GameObjects is supported
                var cube = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Cube](PrimitiveType.Cube.html));
                cube.transform.parent = prefabRoot.transform;
                cube.name = "D";  
      
                // Adding and removing components are supported
                prefabRoot.AddComponent<[AudioSource](AudioSource.html)>();
            }  
      
            // Prefab [Asset](VersionControl.Asset.html) now looks like this:
            // Root
            //    A
            //       B
            //    D
        }
    }
    

### Properties

[assetPath](PrefabUtility.EditPrefabContentsScope-assetPath.html)| File path
of the Prefab asset.  
---|---  
[prefabContentsRoot](PrefabUtility.EditPrefabContentsScope-
prefabContentsRoot.html)| The root GameObject of the Prefab contents.  
  
### Constructors

[PrefabUtility.EditPrefabContentsScope](PrefabUtility.EditPrefabContentsScope-
ctor.html)|  
---|---  
  
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

