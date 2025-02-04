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

#  [SketchUpImporter](SketchUpImporter.html).GetScenes

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

[Switch to Manual](../Manual/class-SketchUpImporter.html "Go to
SketchUpImporter Component in the Manual")

## Declaration

public SketchUpImportScene[] GetScenes();

### Returns

**SketchUpImportScene[]** Array of scenes extracted from a SketchUp file.

### Description

The method returns an array of SketchUpImportScene which represents SketchUp
scenes.

[SketchUpImportScene](SketchUpImportScene.html) is the structure to represent
the Scene that was extracted from the SketchUp file.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class SketchUpUtility
    {
        public static void PrintSketchUpSceneName([GameObject](GameObject.html) go)
        {
            string assetPath = [AssetDatabase.GetAssetPath](AssetDatabase.GetAssetPath.html)(go); // get asset path
            // get [SketchUpImporter](SketchUpImporter.html)
            [SketchUpImporter](SketchUpImporter.html) importer = [AssetImporter.GetAtPath](AssetImporter.GetAtPath.html)(assetPath) as [SketchUpImporter](SketchUpImporter.html);
            if (importer == null)
            {
                [Debug.Log](Debug.Log.html)("This object is not imported by [SketchUpImporter](SketchUpImporter.html)");
                return;
            }  
      
            [SketchUpImportScene](SketchUpImportScene.html)[] scenes = importer.GetScenes();  // get all the scenes  
      
            foreach ([SketchUpImportScene](SketchUpImportScene.html) scene in scenes)
            {
                [Debug.Log](Debug.Log.html)(scene.name);
            }
        }
    }
    

The above example takes a GameObject that is imported from a SketchUp file and
prints the name of the scenes in the SketchUp file.

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

