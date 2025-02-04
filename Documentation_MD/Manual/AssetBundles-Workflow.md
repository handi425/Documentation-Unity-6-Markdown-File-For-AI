[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/AssetBundles-Workflow.html)
  * [中文](/cn/current/Manual/AssetBundles-Workflow.html)
  * [日本語](/ja/current/Manual/AssetBundles-Workflow.html)
  * [한국어](/kr/current/Manual/AssetBundles-Workflow.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/AssetBundles-Workflow.html)
  * [中文](/cn/current/Manual/AssetBundles-Workflow.html)
  * [日本語](/ja/current/Manual/AssetBundles-Workflow.html)
  * [한국어](/kr/current/Manual/AssetBundles-Workflow.html)

  * [Working in Unity](working-in-unity.html)
  * [Assets and media](assets-and-media.html)
  * [Asset workflow](AssetWorkflow.html)
  * [AssetBundles](AssetBundlesIntro.html)
  * AssetBundle workflow

[](AssetBundlesIntro.html)

AssetBundles

[](AssetBundles-Preparing.html)

Preparing Assets for AssetBundles

# AssetBundle workflow

To get started with AssetBundles, follow these steps. More detailed
information about each piece of the workflow can be found in the other pages
in this section of documentation.

**Note** : This section describes the creation of AssetBundles using the
built-in
[BuildPipeline.BuildAssetBundles](../ScriptReference/BuildPipeline.BuildAssetBundles.html)
API. A recommended, and more user friendly, alternative is to use the
[Addressables](http://docs.unity3d.com/Packages/com.unity.addressables@latest/index.html)
package.

## Assigning Assets to AssetBundles

To assign a given Asset to an AssetBundle, follow these steps:

  1. Select the Asset you want to assign to a bundle from your Project View.
  2. Examine the object in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector).

  3. At the bottom of the Inspector, there is a section to assign AssetBundles and Variants. Use the left-hand drop down to assign the AssetBundle, and the right-hand drop down to assign the variant.
  4. Click **None** on the left-hand drop to reveal the currently registered AssetBundle names.
  5. Click **New** to create a new AssetBundle
  6. Type in the desired AssetBundle name. **Note:** AssetBundle names support a type of folder structure depending on what you type. To add sub-folders, separate folder names by a `/`. For example, use the AssetBundle name `environment/forest` to create a bundle named `forest` under an `environment` sub-folder
  7. Once you’ve selected or created an AssetBundle name, you can repeat this process for the right hand drop down to assign or create a Variant name, if you desire. Variant names are not required to build the AssetBundles

**Note:** In the Inspector you can assign an AssetBundle to a folder in your
Project. By default, all Assets in that folder are assigned to the same
AssetBundle as the folder. The AssetBundle assignments for individual Assets
takes precedence, however.

To read more information on AssetBundle assignments and accompanying
strategies, see documentation on [Preparing Assets for
AssetBundles](AssetBundles-Preparing.html).

## Build the AssetBundles

Create a folder called Editor in the Assets folders, and place a script with
the following contents in the folder:

    
    
    using UnityEditor;
    using System.IO;
    
    public class CreateAssetBundles
    {
        [MenuItem("Assets/Build AssetBundles")]
        static void BuildAllAssetBundles()
        {
            string assetBundleDirectory = "Assets/AssetBundles";
            if(!Directory.Exists(assetBundleDirectory))
                Directory.CreateDirectory(assetBundleDirectory);
    
            BuildPipeline.BuildAssetBundles(assetBundleDirectory,
                                            BuildAssetBundleOptions.None,
                                            BuildTarget.StandaloneWindows);
        }
    }
    

This script creates a menu item at the bottom of the Assets menu called
**Build AssetBundles**. When you click **Build AssetBundles** the
BuildAllAssetBundles() function is called. A progress bar appears while the
build takes all the Assets you labeled with an AssetBundle name and uses them
to populate AssetBundles at the path that `assetBundleDirectory` defines.

Let’s take a closer look at the arguments passed to
BuildPipeline.BuildAssetBundles:

_assetBundleDirectory_ : This is the directory that the AssetBundles will be
output to, e.g. “Assets/AssetBundles” within the current Unity project. The
folder does not need to be inside the Assets folder, you can change this to
any output directory you desire. Notice how our script creates the folder on
demand if it does not exist yet.

_BuildAssetBundleOptions.None_ : This is the default value for the build
options argument. You can use this argument to specify one or more flags to
enable a variety of optional behaviours. For example, this argument controls
the choice of **compression** A method of storing data that reduces the amount
of storage space it requires. See [Texture Compression](class-
TextureImporterOverride), [Animation Compression](class-
AnimationClip.html#AssetProperties), [Audio Compression](class-
AudioClip.html), [Build Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression) algorithm, see [AssetBundle
compression](AssetBundles-Cache.html). See
[BuildAssetBundleOptions](../ScriptReference/BuildAssetBundleOptions.html) for
a full listing of the available options.

_BuildTarget.StandaloneWindows_ : Here we’re telling the build pipeline which
target platform we are going to be using these AssetBundles for. You can find
a list of the available build targets in the Scripting API Reference for
[BuildTarget](../ScriptReference/BuildTarget.html). Alternatively, rather than
hardcoding your build target you could call
`EditorUserBuildSettings.activeBuildTarget`, which returns the platform
profile currently set as active in the [Build Profiles](build-profiles.html)A
set of customizable configuration settings to use when creating a build for
your target platform. [More info](build-profiles.html)  
See in [Glossary](Glossary.html#Buildprofile) window.

## Using a Script to Define AssetBundles Contents

The example above describes how to use the Inspector to assign assets to
AssetBundles. You can also assign assets to AssetBundles in code, using a
signature of
[BuildPipeline.BuildAssetBundles](../ScriptReference/BuildPipeline.BuildAssetBundles.html)
that accepts an array of
[AssetBundleBuild](../ScriptReference/AssetBundleBuild.html) structures. If
you use this technique, the data you pass in takes priority, and any
assignments to AssetBundles made in the Inspector are ignored. If you want
your custom script to make use of AssetBundle assignments made in the
Inspector then you can call
[AssetDatabase.GetAllAssetBundleNames](../ScriptReference/AssetDatabase.GetAllAssetBundleNames.html)
and
[AssetDatabase.GetAssetPathsFromAssetBundle](../ScriptReference/AssetDatabase.GetAssetPathsFromAssetBundle.html),
then use that info to populate the AssetBundleBuild array.

## Downloading and Loading AssetBundles and Assets

AssetBundles can be distributed in several ways:

  * Locating the files inside the [StreamingAssets](StreamingAssets.html) folder and including them with your Player build.
  * Hosted by a web service such as Unity’s Cloud Content Delivery and downloaded using [UnityWebRequestAssetBundle](../ScriptReference/UnityWebRequestAssetBundle.html).
  * Distributed by your own download or installation code. This approach takes more development work but does give flexibility to completely control aspects like compression, caching, [patching](AssetBundles-Patching.html) and validation prior to loading the file using Unity APIs.

Depending how the files are distributed you should either use AssetBundle.Load
APIs or UnityWebRequestAssetBundle to load an AssetBundle and access the
AssetBundle object in your runtime code.

From the AssetBundle object, you call one of the LoadAsset methods. For
example, `LoadAsset<T>(string)` which takes the type, `T`, of the asset you’re
attempting to load and the name of the Asset (typically its path). You can use
the returned object just like any object inside of Unity. For example, if you
load a prefab then LoadAsset will return the prefab’s root GameObject, which
you can then instantiate into your current scene by calling `Instantiate()`.

You can reclaim memory used by a loaded AssetBundle by calling
[AssetBundle.Unload(bool)](../ScriptReference/AssetBundle.Unload.html) or
[AssetBundle.UnloadAsync(bool)](../ScriptReference/AssetBundle.Unload.html).

For more information on APIs that load and unload AssetBundles, see
documentation on [Using AssetBundles Natively](AssetBundles-Native.html).

[](AssetBundlesIntro.html)

AssetBundles

[](AssetBundles-Preparing.html)

Preparing Assets for AssetBundles

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

