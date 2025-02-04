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

#  [Undo](Undo.html).RegisterImporterUndo

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

public static void RegisterImporterUndo(string path, string name);

### Parameters

path | Path of the asset importer to register for Undo.  
---|---  
name | The name of the undo operation.  
  
### Description

Copies the state of the importer for the given asset path.

This method is used to Undo a
[AssetDatabase.SetImporterOverride](AssetDatabase.SetImporterOverride.html)
operation.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using UnityEditor.AssetImporters;
    using UnityEditor.Experimental;  
      
    [[ScriptedImporter](AssetImporters.ScriptedImporter.html)(1, null, new[] {"fbx"})]
    class MyFBXImporter : [ScriptedImporter](AssetImporters.ScriptedImporter.html)
    {
        public override void OnImportAsset([AssetImportContext](AssetImporters.AssetImportContext.html) ctx)
        {
            var go = new [GameObject](GameObject.html)("root");
            ctx.AddObjectToAsset("root", go);
            ctx.SetMainObject(go);
        }
    }  
      
    class ChangeImporterOverrideWithUndo
    {
        [[MenuItem](MenuItem.html)("Assets/Change Importer To MyFBXImporter With [Undo](Undo.html)")]
        static void ChangeImporterWithUndo()
        {
            var assetPath = [AssetDatabase.GetAssetPath](AssetDatabase.GetAssetPath.html)([Selection.activeObject](Selection-activeObject.html));
            [Undo.RegisterImporterUndo](Undo.RegisterImporterUndo.html)(assetPath, "Changed Importer");
            [AssetDatabase.SetImporterOverride](AssetDatabase.SetImporterOverride.html)<MyFBXImporter>(assetPath);
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

