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

#  [AssetDatabase](AssetDatabase.html).ForceReserializeAssets

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

public static void ForceReserializeAssets();

## Declaration

public static void ForceReserializeAssets(IEnumerable<string> assetPaths,
[ForceReserializeAssetsOptions](ForceReserializeAssetsOptions.html) options);

### Parameters

assetPaths | The paths to the assets that should be reserialized.  
---|---  
options | Specify whether you want to reserialize the assets themselves, their .meta files, or both. If omitted, defaults to both.  
  
### Description

Forcibly load and re-serialize the given assets, flushing any outstanding data
changes to disk.

When Unity loads old data from an asset or Scene file, the data is dynamically
upgraded in memory, but not written back to disk unless the user does
something that explicitly dirties the object (like changing a value on it).
This method allows you to proactively load, upgrade, and write back to disk
any asset or Scene files in the project, without having to manually make them
dirty.  
  
Unity's usual behaviour has a number of benefits, particularly for projects
with version control systems, where upgrading all the assets proactively after
moving to a new Unity version would result in massive lists of changed files
to be committed. However, it also has the drawback of upgrades being 'mixed
in' with deliberate changes as users continue to work on a project. This
method allows you to be proactive in a controlled way, deciding exactly which
assets you want to upgrade and when.  
  
Note: You should only call this method from direct user actions, such as a
menu item. You should not call ForceReserializeAssets from a Unity callback
(such as OnEnable), because it might be called while a scene is being
modified. If you do this, Unity throws an exception.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class AssetDatabaseExamples : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("[AssetDatabase](AssetDatabase.html)/Force Reserialize Assets Example")]
        static void UpdateGroundMaterials()
        {
            for (var i = 0; i < 10; i++)
            {
                var matPath = $"Assets/Materials/GroundMaterial{i}.mat";
                var mat = ([Material](Material.html))[AssetDatabase.LoadMainAssetAtPath](AssetDatabase.LoadMainAssetAtPath.html)(matPath);
                [AssetImporter.GetAtPath](AssetImporter.GetAtPath.html)(matPath).SetAssetBundleNameAndVariant("GroundBundle", "");
                mat.shader = [Shader.Find](Shader.Find.html)("Standard");
                mat.color = [Color.white](Color-white.html);
                mat.mainTexture = ([Texture](Texture.html))[AssetDatabase.LoadMainAssetAtPath](AssetDatabase.LoadMainAssetAtPath.html)($"Assets/Textures/GroundTexture{i}.jpg");
            }
            [AssetDatabase.ForceReserializeAssets](AssetDatabase.ForceReserializeAssets.html)();  
      
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

