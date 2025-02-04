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

#  [AssetDatabase](AssetDatabase.html).GetAssetDependencyHash

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

public static [Hash128](Hash128.html) GetAssetDependencyHash(string path);

## Declaration

public static [Hash128](Hash128.html) GetAssetDependencyHash(GUID guid);

### Parameters

path | Path to the asset.  
---|---  
guid | GUID of the asset.  
  
### Returns

**Hash128** Aggregate hash.

### Description

Returns the hash of all the dependencies of an asset.

The hash aggregates the following: source asset path, source asset, meta file,
target platform and importer version. The change of this hash indicates that
the imported asset may have changed so the relevant asset bundles should be
rebuilt.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class AssetDatabaseExamples : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("[AssetDatabase](AssetDatabase.html)/Dependency Hash Example")]
        public static void DependencyHashExample()
        {
            //Load a [Material](Material.html), change its shader and save it
            var matPath = "Assets/Material.mat";
            var asset = ([Material](Material.html))[AssetDatabase.LoadMainAssetAtPath](AssetDatabase.LoadMainAssetAtPath.html)(matPath);
            asset.shader = [Shader.Find](Shader.Find.html)("Unlit/[Texture](Texture.html)");
            [AssetDatabase.SaveAssets](AssetDatabase.SaveAssets.html)();  
      
            //Print out the hash into the console
            var hash = [AssetDatabase.GetAssetDependencyHash](AssetDatabase.GetAssetDependencyHash.html)(matPath);
            [Debug.Log](Debug.Log.html)(hash);  
      
            //Change the [Shader](Shader.html) on the [Material](Material.html) and save it
            asset.shader = [Shader.Find](Shader.Find.html)("Standard");
            [AssetDatabase.SaveAssets](AssetDatabase.SaveAssets.html)();  
      
            //Hash will be different
            hash = [AssetDatabase.GetAssetDependencyHash](AssetDatabase.GetAssetDependencyHash.html)(matPath);
            [Debug.Log](Debug.Log.html)(hash);
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

