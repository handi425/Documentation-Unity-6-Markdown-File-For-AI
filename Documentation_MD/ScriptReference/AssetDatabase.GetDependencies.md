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

#  [AssetDatabase](AssetDatabase.html).GetDependencies

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

public static string[] GetDependencies(string pathName);

## Declaration

public static string[] GetDependencies(string pathName, bool recursive);

### Parameters

pathName | The path to the asset for which dependencies are required.  
---|---  
recursive | Controls whether this method recursively checks and returns all dependencies including indirect dependencies (when set to true), or whether it only returns direct dependencies (when set to false).  
  
### Returns

**string[]** The paths of all assets that the input depends on.

### Description

Returns an array of all the assets that are dependencies of the asset at the
specified **pathName**.  
  
**Note:** [GetDependencies](AssetDatabase.GetDependencies.html)() gets the
Assets that are referenced by other Assets. For example, a Scene could contain
many GameObjects with a Material attached to them. In this case,
[GetDependencies](AssetDatabase.GetDependencies.html)() will return the path
to the Material Assets, but not the GameObjects as those are not Assets on
your disk.

If **recursive** is true, the list returned will also include the input path
itself. Note that this function returns all assets that are referenced by the
input asset; these references are not necessarily required during the build
process.

* * *

## Declaration

public static string[] GetDependencies(string[] pathNames);

## Declaration

public static string[] GetDependencies(string[] pathNames, bool recursive);

### Parameters

pathNames | The path to the assets for which dependencies are required.  
---|---  
recursive | Controls whether this method recursively checks and returns all dependencies including indirect dependencies (when set to true), or whether it only returns direct dependencies (when set to false).  
  
### Returns

**string[]** The paths of all assets that the input depends on.

### Description

Returns an array of the paths of assets that are dependencies of all the
assets in the list of **pathName** s that you provide.  
  
**Note:** [GetDependencies](AssetDatabase.GetDependencies.html)() gets the
Assets that are referenced by other Assets. For example, a Scene could contain
many GameObjects with a Material attached to them. In this case,
[GetDependencies](AssetDatabase.GetDependencies.html)() will return the path
to the Material Assets, but not the GameObjects as those are not Assets on
your disk.

If **recursive** is true, the list returned will also include the input paths
themselves. Note that this function returns all assets that are referenced by
the input asset; these references are not necessarily required during the
build process.

    
    
    using System.Text;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class GetDependenciesExample : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("APIExamples/GetDependencies")]
        static void GetAllDependenciesForScenes()
        {
            var allScenes = [AssetDatabase.FindAssets](AssetDatabase.FindAssets.html)("t:[Scene](SceneManagement.Scene.html)");
            string[] allPaths = new string[allScenes.Length];
            int curSceneIndex = 0;  
      
            foreach (var guid in allScenes)
            {
                var path = [AssetDatabase.GUIDToAssetPath](AssetDatabase.GUIDToAssetPath.html)(guid);
                allPaths[curSceneIndex] = path;
                ++curSceneIndex;
            }  
      
            var dependencies = [AssetDatabase.GetDependencies](AssetDatabase.GetDependencies.html)(allPaths);  
      
            StringBuilder dependenciesString = new StringBuilder();
            dependenciesString.AppendLine();  
      
            foreach (var curDependency in dependencies)
            {
                dependenciesString.Append(curDependency);
                dependenciesString.AppendLine();
            }  
      
            [Debug.Log](Debug.Log.html)("All dependencies for Scenes in Project: " + dependenciesString);
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

