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
[BuildAssetBundleOptions](BuildAssetBundleOptions.html).ChunkBasedCompression

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

Use chunk-based LZ4 compression when creating the AssetBundle.

When chunk-based compression is used, the content of the AssetBundle is broken
into individual segments, which are compressed independently using the
[CompressionType.Lz4HC](CompressionType.Lz4HC.html) algorithm. The resulting
file is typically larger than the full-file compression which is used by
default, but AssetBundles built with this format can be loaded incrementally,
e.g. without decompressing the full contents into memory. This is the default
format used for AssetBundles stored in the AssetBundle Cache.  
  
Additional resources: [AssetBundles compression](../Manual/AssetBundles-
Cache.html), [BuildCompression](BuildCompression.html),
[CompressionType](CompressionType.html),
[ArchiveHandle.Compression](Unity.IO.Archive.ArchiveHandle.Compression.html),
[Caching](Caching.html),
[BuildAssetBundleOptions.UncompressedAssetBundle](BuildAssetBundleOptions.UncompressedAssetBundle.html),
[BuildOptions.CompressWithLz4](BuildOptions.CompressWithLz4.html).

    
    
    //Create a folder (right click in the Assets folder and go to **Create** >**Folder**), and name it “[Editor](Editor.html)” if it doesn’t already exist
    //Place this script in the [Editor](Editor.html) folder  
      
    //This script creates a new [Menu](Menu.html) named “Build [Asset](VersionControl.Asset.html)” and new options within the menu named “Normal” and “Chunk Based Compression”. Click these menu items to build an [AssetBundle](AssetBundle.html).  
      
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
      
        //Creates a new item (Chunk Based Compression) in the new Build [Asset](VersionControl.Asset.html) Bundles menu
        [[MenuItem](MenuItem.html)("Build [Asset](VersionControl.Asset.html) Bundles/Chunk Based Compression")]
        static void BuildABsChunk()
        {
            //Build the AssetBundles in this mode
            [BuildPipeline.BuildAssetBundles](BuildPipeline.BuildAssetBundles.html)("Assets/MyAssetBuilds", [BuildAssetBundleOptions.ChunkBasedCompression](BuildAssetBundleOptions.ChunkBasedCompression.html), [BuildTarget.StandaloneOSX](BuildTarget.StandaloneOSX.html));
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

