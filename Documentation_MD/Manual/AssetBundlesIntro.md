[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/AssetBundlesIntro.html)
  * [中文](/cn/current/Manual/AssetBundlesIntro.html)
  * [日本語](/ja/current/Manual/AssetBundlesIntro.html)
  * [한국어](/kr/current/Manual/AssetBundlesIntro.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/AssetBundlesIntro.html)
  * [中文](/cn/current/Manual/AssetBundlesIntro.html)
  * [日本語](/ja/current/Manual/AssetBundlesIntro.html)
  * [한국어](/kr/current/Manual/AssetBundlesIntro.html)

  * [Working in Unity](working-in-unity.html)
  * [Assets and media](assets-and-media.html)
  * [Asset workflow](AssetWorkflow.html)
  * AssetBundles

[](DefaultPresetsByFolder.html)

Applying default presets to Assets by folder

[](AssetBundles-Workflow.html)

AssetBundle workflow

# AssetBundles

An **AssetBundle** is an archive file that contains platform-specific non-code
Assets (such as Models, Textures, Prefabs, Audio clips, and even entire
Scenes) that Unity can load at run time. AssetBundles can express dependencies
between each other; for example, a Material in one AssetBundle can reference a
Texture in another AssetBundle. For efficient delivery over networks, you can
compress AssetBundles with a choice of built-in algorithms depending on use
case requirements (LZMA and LZ4).

AssetBundles can be useful for downloadable content (DLC), reducing initial
install size, loading assets optimized for the end-user’s platform, and reduce
runtime memory pressure.

An AssetBundle built for any of the standalone platforms can only be loaded on
that platform. For example, a bundle built on iOS is not compatible with
Android. One reason for this is that **Shaders** A program that runs on the
GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader), Textures and other types of data are
built into platform-specific formats based on the
[BuildTarget](../ScriptReference/BuildTarget.html).

When you build or rebuild AssetBundles, you typically build all of the
project’s AssetBundles together using a single API call. It is usually best
not to build or rebuild them individually, because when built together, the
Unity Editor makes decisions about how to reference or embed content in each
AssetBundle which can depend on what is included in other AssetBundles. The
exception to this is if you’re an advanced user who understands the references
and dependencies among the AssetBundles in your project, in which case you can
sometimes build just a subset of your project’s AssetBundles.

## What’s inside an AssetBundle?

Because the APIs that you use to load AssetBundles are designed to be simple,
they abstract away the details of how data is represented inside AssetBundles.
However it can be useful to understand the structure, especially if you use
tools to extract or examine the contents of an AssetBundle.

The AssetBundle is a container file format, similar to a zip file. It has a
binary-format header and embeds additional files inside it. These additional
files consist of two types:

  * Serialized files, which contains serialized Unity objects. This is the same binary file format used in Player Builds. In the case of an AssetBundle containing Assets all the objects are written to a single Serialized File. For AssetBundles containing Scenes there are two serialized files per **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene), one with the objects from the scene
hierarchy and the second with any referenced objects.

  * Resource files, which are chunks of binary data stored separately for certain Assets (textures and audio). This separation allows Unity to efficiently load them from disk using multi-threaded code.

The AssetBundle file always includes a serialized
[AssetBundle](../ScriptReference/AssetBundle.html) object. This object acts
like a directory for the contents of the AssetBundle. This is the object you
interact with via code to load Assets from a specific AssetBundle archive, and
it is also used internally when loading Assets from AssetBundles with the
Addressables API.

## Backward compatibility

When an AssetBundle is built, the objects that are included are serialized
using the definition from the version of the Unity Editor you used to build
it, as well as the C# types defined in the Project that is built. The
information for each type is recorded inside the AssetBundle in a structure
called the _Type Tree_. This type information contributes somewhat to the size
of the AssetBundle, but it is critical to enabling loading those objects when
the version of the player does not match the Editor version at the time of the
build. For many Unity features the types are quite stable and only change in
minor ways between versions so the backward compatibility support works well.
However in cases where Unity features change substantially it may not be
possible to load the old data in a way that achieves the expected results in
the newer version. In that case, you must rebuild the AssetBundle using the
new version of Unity.

Unity does not support forward-compatibility, so loading an AssetBundle built
with a new version of Unity into a Player that was built with an older version
of Unity is likely to have trouble loading the content.

**Note:** By default the version of the Unity Editor that was used to build
the file is included inside the AssetBundle header. This information can be
useful when investigating backward compatibility issues. However, it can also
result in AssetBundles being rebuilt unnecessarily, and cause unnecessary
client downloads if a project is rebuilt after doing a minor upgrade of the
Editor. To avoid this, you can exclude the Editor version, see
[BuildAssetBundleOptions.AssetBundleStripUnityVersion](../ScriptReference/BuildAssetBundleOptions.AssetBundleStripUnityVersion.html).

## Support for Script Objects

AssetBundles do not contain assemblies and are not used to distribute new C#
classes or changes to existing classes. Rather, it is the Player Build that
contains the compiled assemblies. This means to release code changes, you must
rebuild and redistribute the main build of your game or app.

However, you can use AssetBundles to distribute new objects that are instances
of the classes compiled into your Player build, such as new items for a game.

For example, AssetBundles can include ScriptableObject Assets. When you load
that Asset from the AssetBundle Unity finds the matching class definition,
based on the assembly name, namespace and class name. It creates an object
that is an instance of that class and sets the fields of the object using the
serialized values.

If the object was serialized based on an older definition of the class then
Unity will use its backward compatibility support to match up whatever fields
it can, based on the field names and other info recorded in the Type Tree.

Scripts often use [Conditional Compilation](platform-dependent-
compilation.html) to specify platform-specific code. For example, using
scripting symbols like UNITY_STANDALONE, UNITY_IOS and UNITY_ANDROID. If
fields on a class or struct are not compiled on some targets then the
serialization of objects inside the AssetBundle will not include those fields
(and they will not be included in the Type Tree). This is another reason that
AssetBundles must be rebuilt for each platform that you target.

## Methods of building AssetBundles

There are two supported APIs to build AssetBundles for Unity:

  * Using built-in native APIs, e.g. `BuildPipeline.BuildAssetBundles`, `AssetBundle` and `UnityWebRequestAssetBundle`. This is the functionality described in this section of the Manual. However this method is quite low-level, for example it requires that you understand Asset dependencies, determine bundle assignments yourself and write your own build script.
  * Using the [Addressables](http://docs.unity3d.com/Packages/com.unity.addressables@latest/index.html) package. This is the recommended, more user friendly option, and makes it possible to define and build AssetBundles directly from the Addressables **UI**(User Interface) Allows a user to interact with your application. Unity currently supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI). It uses the same underlying file format
and the same low-level Unity loading and caching services, but indirectly via
a higher-level, more abstract API. So, while many of the concepts describes in
this section apply to AssetBundles used with Addressables, you should refer to
the Addressables documentation for practical usage information.

[](DefaultPresetsByFolder.html)

Applying default presets to Assets by folder

[](AssetBundles-Workflow.html)

AssetBundle workflow

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

