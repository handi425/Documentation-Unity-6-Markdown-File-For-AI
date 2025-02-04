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

#  [AssetDatabase](AssetDatabase.html).GenerateUniqueAssetPath

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

public static string GenerateUniqueAssetPath(string path);

### Description

Creates a new unique path for an asset.

When you call this method, Unity checks to see whether an asset already exists
with the matching path and filename you supply. If it does not exist, Unity
returns the same string you supplied. If there is already an existing asset
with the matching path and filename, Unity appends the number 1 to the
filename and checks again. It continues incrementing this number and checking
again until it finds a filename that does not currently exists, and returns
the path with that new unique filename.  
  
All paths generated are relative to the project folder, for example:
"Assets/MyTextures/hello.png".

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class GenerateUniqueAssetPathExample : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("APIExamples/GenerateUniqueAssetPath")]
        static void GenerateUniqueAssetPathForFilesWithSameName()
        {
            for (int i = 0; i < 5; ++i)
            {
                //The file names that this should create are:
                // Assets/Artifacts/material.mat
                // Assets/Artifacts/material 1.mat
                // Assets/Artifacts/material 2.mat
                // Assets/Artifacts/material 3.mat
                // Assets/Artifacts/material 4.mat
                var uniqueFileName = [AssetDatabase.GenerateUniqueAssetPath](AssetDatabase.GenerateUniqueAssetPath.html)("Assets/Artifacts/material.mat");  
      
                [Material](Material.html) material = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Specular"));
                [AssetDatabase.CreateAsset](AssetDatabase.CreateAsset.html)(material, uniqueFileName);
            }
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

