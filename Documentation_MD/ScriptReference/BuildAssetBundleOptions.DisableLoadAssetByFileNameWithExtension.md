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

#
[BuildAssetBundleOptions](BuildAssetBundleOptions.html).DisableLoadAssetByFileNameWithExtension

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

Disables Asset Bundle LoadAsset by file name with extension.

Asset Bundles by default have three ways to look up the same asset: full asset
path, asset file name, and asset file name with extension. The full path is
serialized into Asset Bundles, while file name and file name with extension
are generated when an Asset Bundle is loaded from file.  
  
Example: "Assets/Prefabs/Player.prefab", "Player", and "Player.prefab"  
  
This option will set a flag on Asset Bundles to prevent creating the asset
file name with extension lookup. This option saves runtime memory and loading
performance for asset bundles.  
  
Additional resources: BuildAssetBundleOptions.DisableFileNameLoading.

    
    
    //Create a folder (right click in the Assets folder and go to **Create** >**Folder**), and name it “[Editor](Editor.html)” if it doesn’t already exist
    //Place this script in the [Editor](Editor.html) folder  
      
    //This script creates a new [Menu](Menu.html) named “Build [Asset](VersionControl.Asset.html)” and new options within the menu named “Normal” and “Disable Load [Asset](VersionControl.Asset.html) By filename with Extension”. Click these menu items to build an [AssetBundle](AssetBundle.html) into a folder.  
      
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class Example
    {
        //Creates a new menu (Build [Asset](VersionControl.Asset.html) Bundles) and item (Normal) in the [Editor](Editor.html)
        [[MenuItem](MenuItem.html)("Build [Asset](VersionControl.Asset.html) Bundles/Normal")]
        static void BuildABsNone()
        {
            //Build AssetBundles with no special options
            //They will be written in the custom folder ("MyAssetBuilds") which needs to exist prior to this call.
            [BuildPipeline.BuildAssetBundles](BuildPipeline.BuildAssetBundles.html)("Assets/MyAssetBuilds", [BuildAssetBundleOptions.None](BuildAssetBundleOptions.None.html), [BuildTarget.StandaloneOSX](BuildTarget.StandaloneOSX.html));
        }  
      
        //Creates a new item (Disable Load [Asset](VersionControl.Asset.html) By Name with Extension) in the new Build [Asset](VersionControl.Asset.html) Bundles menu
        [[MenuItem](MenuItem.html)("Build [Asset](VersionControl.Asset.html) Bundles/Disable Load [Asset](VersionControl.Asset.html) By Name with Extension ")]
        static void BuildABsDisable()
        {
            //Build the AssetBundles in this mode
            [BuildPipeline.BuildAssetBundles](BuildPipeline.BuildAssetBundles.html)("Assets/MyAssetBuilds", [BuildAssetBundleOptions.DisableLoadAssetByFileNameWithExtension](BuildAssetBundleOptions.DisableLoadAssetByFileNameWithExtension.html), [BuildTarget.StandaloneOSX](BuildTarget.StandaloneOSX.html));
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

