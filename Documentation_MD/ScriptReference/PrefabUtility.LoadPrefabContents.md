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

#  [PrefabUtility](PrefabUtility.html).LoadPrefabContents

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

public static [GameObject](GameObject.html) LoadPrefabContents(string
assetPath);

### Parameters

assetPath | The path of the Prefab Asset to load the contents of.  
---|---  
  
### Returns

**GameObject** The root of the loaded contents.

### Description

Loads a Prefab Asset at a given path into an isolated Scene and returns the
root GameObject of the Prefab.

You can use this to get the content of the Prefab and modify it directly
instead of going through an instance of the Prefab. This is useful for batch
operations.  
  
Once you have modified the Prefab you have to write it back using
[SaveAsPrefabAsset](PrefabUtility.SaveAsPrefabAsset.html) and then call
[UnloadPrefabContents](PrefabUtility.UnloadPrefabContents.html) to release the
Prefab and isolated Scene from memory.  
  
Additional resources:
[EditPrefabContentsScope](PrefabUtility.EditPrefabContentsScope.html).

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class Example
    {
        [[MenuItem](MenuItem.html)("Examples/Add [BoxCollider](BoxCollider.html) to Prefab [Asset](VersionControl.Asset.html)")]
        static void AddBoxColliderToPrefab()
        {
            // Get the Prefab [Asset](VersionControl.Asset.html) root [GameObject](GameObject.html) and its asset path.
            [GameObject](GameObject.html) assetRoot = [Selection.activeObject](Selection-activeObject.html) as [GameObject](GameObject.html);
            string assetPath = [AssetDatabase.GetAssetPath](AssetDatabase.GetAssetPath.html)(assetRoot);  
      
            // Load the contents of the Prefab [Asset](VersionControl.Asset.html).
            [GameObject](GameObject.html) contentsRoot = [PrefabUtility.LoadPrefabContents](PrefabUtility.LoadPrefabContents.html)(assetPath);  
      
            // Modify Prefab contents.
            contentsRoot.AddComponent<[BoxCollider](BoxCollider.html)>();  
      
            // Save contents back to Prefab [Asset](VersionControl.Asset.html) and unload contents.
            [PrefabUtility.SaveAsPrefabAsset](PrefabUtility.SaveAsPrefabAsset.html)(contentsRoot, assetPath);
            [PrefabUtility.UnloadPrefabContents](PrefabUtility.UnloadPrefabContents.html)(contentsRoot);
        }  
      
        [[MenuItem](MenuItem.html)("Examples/Add [BoxCollider](BoxCollider.html) to Prefab [Asset](VersionControl.Asset.html)", true)]
        static bool ValidateAddBoxColliderToPrefab()
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

