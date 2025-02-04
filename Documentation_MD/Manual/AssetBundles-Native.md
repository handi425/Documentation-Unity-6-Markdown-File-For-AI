[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/AssetBundles-Native.html)
  * [中文](/cn/current/Manual/AssetBundles-Native.html)
  * [日本語](/ja/current/Manual/AssetBundles-Native.html)
  * [한국어](/kr/current/Manual/AssetBundles-Native.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/AssetBundles-Native.html)
  * [中文](/cn/current/Manual/AssetBundles-Native.html)
  * [日本語](/ja/current/Manual/AssetBundles-Native.html)
  * [한국어](/kr/current/Manual/AssetBundles-Native.html)

  * [Working in Unity](working-in-unity.html)
  * [Assets and media](assets-and-media.html)
  * [Asset workflow](AssetWorkflow.html)
  * [AssetBundles](AssetBundlesIntro.html)
  * Using AssetBundles Natively

[](AssetBundles-Building.html)

Output of the Build

[](AssetBundles-Cache.html)

AssetBundle compression and caching

# Using AssetBundles Natively

There are two different APIs that you can use to load AssetBundles.

  * The static Load methods on the AssetBundle object, for example [AssetBundle.LoadFromFile](../ScriptReference/AssetBundle.LoadFromFile.html).
  * The UnityWebRequest support for AssetBundles, e.g. [UnityWebRequestAssetBundle.GetAssetBundle](../ScriptReference/Networking.UnityWebRequestAssetBundle.GetAssetBundle.html).

## AssetBundle.LoadFromFile

[AssetBundle.LoadFromFile](../ScriptReference/AssetBundle.LoadFromFile.html)

This API is highly-efficient when loading uncompressed and chunk compressed
bundles (LZ4) from local storage because it can read content of the file
incrementally, directly from disk. Loading a file that is compressed with full
file **compression** A method of storing data that reduces the amount of
storage space it requires. See [Texture Compression](class-
TextureImporterOverride), [Animation Compression](class-
AnimationClip.html#AssetProperties), [Audio Compression](class-
AudioClip.html), [Build Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression) (LZMA) using this method is less
efficient because it requires that the file be fully decompressed into memory
first.

One example of how to use `LoadFromFile`:

    
    
    using System.IO;
    using UnityEngine;
    
    public class LoadFromFileExample : MonoBehaviour
    {
        void Start()
        {
            var myLoadedAssetBundle = AssetBundle.LoadFromFile(Path.Combine(Application.streamingAssetsPath, "myassetBundle"));
    
            if (myLoadedAssetBundle == null)
            {
                Debug.Log("Failed to load AssetBundle!");
                return;
            }
            var prefab = myLoadedAssetBundle.LoadAsset<GameObject>("MyObject");
            Instantiate(prefab);
        }
    }
    

Rather than blocking your app during the load process you can also use the
asynchronous version, `AssetBundle.LoadFromFileAsync`.

There are several other methods available to load an AssetBundle if it is not
actually stored in a local file. For example you can use
[AssetBundle.LoadFromMemoryAsync](../ScriptReference/AssetBundle.LoadFromMemoryAsync.html).

## UnityWebRequestAssetBundle

The
[UnityWebRequestAssetBundle](../ScriptReference/Networking.UnityWebRequestAssetBundle.GetAssetBundle.html)
API can be called to create a special web request for downloading, caching and
loading AssetBundles.

Typically the URL would be a ‘https://’ address pointing to the file as
exposed by a web service. It could also be ‘file://’ to access local data on
platforms that do not support direct file system access.

This request can be passed into
[DownloadHandlerAssetBundle.GetContent(UnityWebRequestAssetBundle)](../ScriptReference/Networking.DownloadHandlerAssetBundle.GetContent.html)
to get the AssetBundle object for the loaded AssetBundle.

For example

    
    
    using System.Collections;
    using UnityEngine;
    using UnityEngine.Networking;
    
    public class DownloadExample : MonoBehaviour
    {
        IEnumerator Start()
        {
            string uri = "https://myserver/myBundles/bundle123";
            uint crc = 1098980; // Expected content CRC
    
            UnityWebRequest request = UnityWebRequestAssetBundle.GetAssetBundle(uri, crc);
            yield return request.SendWebRequest();
    
            AssetBundle bundle = DownloadHandlerAssetBundle.GetContent(request);
            var loadAsset = bundle.LoadAssetAsync<GameObject>("Assets/Players/MainPlayer.prefab");
            yield return loadAsset;
    
            Instantiate(loadAsset.asset);
        }
    }
    

or starting in 2023.1 with Await support:

    
    
    using System.Collections;
    using UnityEngine;
    using UnityEngine.Networking;
    
    public class DownloadExample : MonoBehaviour
    {
        async void Start()
        {
            string uri = "https://myserver/myBundles/bundle123";
            uint crc = 1098980; // Expected content CRC
    
            UnityWebRequest request = UnityWebRequestAssetBundle.GetAssetBundle(uri, crc);
            await request.SendWebRequest();
    
            AssetBundle bundle = DownloadHandlerAssetBundle.GetContent(request);
            var loadAsset = bundle.LoadAssetAsync<GameObject>("Assets/Players/MainPlayer.prefab");
            await loadAsset;
    
            Instantiate(loadAsset.asset);
        }
    }
    

For simplicity the example shows a CRC value that is hardcoded in the code.
But in practice the expected CRC values for your AssetBundles would be
downloaded separately, or retrieved from a file, prior to downloading the
AssetBundles. See [AssetBundle Download Integrity and Security](AssetBundles-
Integrity.html).

**Note:** In order to avoid downloading the entire AssetBundle content each
time this code is called you could enable caching for your AssetBundle. This
is done by passing the AssetBundle hash when calling
UnityWebRequestAssetBundle.GetAssetBundle. The hash is available from the
AssetBundle Manifest, which is described later in this section. The hash acts
as version identifier for the precise build of the AssetBundle that you are
requesting. See [AssetBundle compression and caching](AssetBundles-Cache.html)
for details of the Cache and the associated considerations about compression.

## Loading Assets from AssetBundles

Now that you’ve successfully loaded your AssetBundle, it’s time to finally
load in some Assets.

Generic code snippet:

    
    
    T objectFromBundle = bundleObject.LoadAsset<T>(assetName);
    

T is the type of the Asset you’re attempting to load.

There are a couple options when deciding how to load Assets. We have
`LoadAsset`, `LoadAllAssets`, and their Async counterparts `LoadAssetAsync`
and `LoadAllAssetsAsync` respectively.

This is how to load an asset from an AssetBundles synchronously:

To load a single Asset (for example the root GameObject of a Prefab):

    
    
    GameObject gameObject = loadedAssetBundle.LoadAsset<GameObject>(assetName);
    

To load all Assets:

    
    
    Unity.Object[] objectArray = loadedAssetBundle.LoadAllAssets();
    

This returns an array with all the root Object of each Asset.

Now, whereas the previously shown methods return either the type of object
you’re loading or an array of objects, the asynchronous methods return an
[AssetBundleRequest](../ScriptReference/AssetBundleRequest.html). You’ll need
to wait for this operation to complete before accessing the asset. To load an
asset asynchronously:

    
    
    AssetBundleRequest request = loadedAssetBundleObject.LoadAssetAsync<GameObject>(assetName);
    yield return request; // or await request;
    var loadedAsset = request.asset;
    

And

    
    
    AssetBundleRequest request = loadedAssetBundle.LoadAllAssetsAsync();
    yield return request; // or await request;
    var loadedAssets = request.allAssets;
    

Once you have loaded your Assets you’re good to go! You’re able to use the
loaded objects as you would any Object in Unity.

#### Loading AssetBundle Manifests

Loading AssetBundle manifests can be incredibly useful. Especially when
dealing with AssetBundle dependencies.

To get a useable
[AssetBundleManifest](../ScriptReference/AssetBundleManifest.html) object,
you’ll need to load that additional AssetBundle (the one that’s named the same
thing as the folder it’s in) and load an object of type AssetBundleManifest
from it.

Loading the manifest itself is done exactly the same as any other Asset from
an AssetBundle:

    
    
    AssetBundle assetBundle = AssetBundle.LoadFromFile(manifestFilePath);
    AssetBundleManifest manifest = assetBundle.LoadAsset<AssetBundleManifest>("AssetBundleManifest");
    

Now you have access to the `AssetBundleManifest` API calls through the
manifest object from the above example. From here you can use the manifest to
get information about the AssetBundles you built. This information includes
dependency data, hash data, and variant data for the AssetBundles.

The earlier section on [AssetBundle Dependencies](AssetBundles-
Dependencies.html) discussed how, in order to load an Asset from an
AssetBundle, you must first load any AssetBundles that the AssetBundle depends
on. The manifest object makes dynamically finding and loading dependencies
possible, so you do not have to hardcode all the AssetBundle names and their
relationships explicitly in your code. Let’s say we want to load all the
dependencies for an AssetBundle named “assetBundle”.

    
    
    AssetBundle assetBundle = AssetBundle.LoadFromFile(manifestFilePath);
    AssetBundleManifest manifest = assetBundle.LoadAsset<AssetBundleManifest>("AssetBundleManifest");
    string[] dependencies = manifest.GetAllDependencies("assetBundle"); //Pass the name of the bundle you want the dependencies for.
    foreach(string dependency in dependencies)
    {
        AssetBundle.LoadFromFile(Path.Combine(assetBundlePath, dependency));
    }
    

Now that you’re loading AssetBundles, AssetBundle dependencies, and Assets,
it’s time to talk about managing all of these loaded AssetBundles.

## Managing Loaded AssetBundles

**Note:** The
[Addressables](http://docs.unity3d.com/Packages/com.unity.addressables@latest/index.html)
package provides a ready-made system to manage loading AssetBundles,
dependencies, and Assets. Unity recommends using Addressables rather than
managing AssetBundles yourself.

See also: Unity Learn tutorial on [Managing Loaded
AssetBundles](https://unity3d.com/fr/learn/tutorials/topics/best-
practices/assetbundle-usage-patterns#Managing_Loaded_Assets)

Unity does not automatically unload Objects when they are removed from the
active **scene** A Scene contains the environments and menus of your game.
Think of each unique Scene file as a unique level. In each Scene, you place
your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). Asset cleanup is triggered at specific
times, and it can also be triggered manually.

It is important to know when to load and unload an AssetBundle. Improperly
unloading an AssetBundle can lead to duplicating objects in memory or missing
objects.

The biggest things to understand about AssetBundle management is when to call
[AssetBundle.Unload(bool)](../ScriptReference/AssetBundle.Unload.html) – or
[AssetBundle.UnloadAsync(bool)](../ScriptReference/AssetBundle.Unload.html) –
and if you should pass true or false into the function call. Unload is a non-
static function that will unload your AssetBundle by removing the AssetBundle
header and other data structures from memory. The argument indicates whether
to also unload all Objects instantiated from this AssetBundle.

`AssetBundle.Unload(true)` unloads all **GameObjects** The fundamental object
in Unity scenes, which can represent characters, props, scenery, cameras,
waypoints, and more. A GameObject’s functionality is defined by the Components
attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) (and their dependencies) that were
loaded from the AssetBundle. This does not include objects that you have
copied into your scene (e.g. by calling `Instantiate`) because that copied
data does not belong to the AssetBundle. If the objects in your scene
references Textures that were loaded from the AssetBundle (and still belong to
it), then this call will cause the Textures to disappear, and Unity treats
them as missing Textures.

As an example, let’s assume Material M is loaded from AssetBundle AB as shown
below and used in **Prefab** An asset type that allows you to store a
GameObject complete with components and properties. The prefab acts as a
template from which you can create new object instances in the scene. [More
info](Prefabs.html)  
See in [Glossary](Glossary.html#Prefab) P.

If AB.Unload(true) is called then any instance of M referenced from objects in
the active scene will be destroyed.

If you were instead to call AB.Unload(false) then the instances of M will
remain in memory. They will become independent objects that are not linked
back to the original AssetBundle.

![](../uploads/Main/AssetBundles-Native-1.png)

If AB is loaded again later Unity will not re-link the existing copies of M to
the Material inside the AssetBundle.

![](../uploads/Main/AssetBundles-Native-2.png)

If you create another instance of Prefab P, it will not use the existing copy
of M. Instead a second copy of M is loaded.

![](../uploads/Main/AssetBundles-Native-3.png)

Generally, using `AssetBundle.Unload(false)` can lead to duplicated objects
and other issues. Most projects should use `AssetBundle.Unload(true)` to avoid
this. There are two common strategies for safely calling
`AssetBundle.Unload(true)`:

  * Having well-defined points during the application’s lifetime at which transient AssetBundles are unloaded, such as between levels or during a loading screen.

  * Maintaining reference-counts for individual Objects and unload AssetBundles only when all of their constituent Objects are unused. This permits an application to unload & reload individual Objects without duplicating memory.

If an application must use `AssetBundle.Unload(false)`, then individual
Objects can only be unloaded in two ways:

  * Eliminate all references to an unwanted Object, e.g. make sure no other loaded object has a field that points to it. After this is done, call [Resources.UnloadUnusedAssets](../ScriptReference/Resources.UnloadUnusedAssets.html).

  * Load a scene non-additively. This will destroy all Objects in the current scene and invoke [Resources.UnloadUnusedAssets](../ScriptReference/Resources.UnloadUnusedAssets.html) automatically.

[](AssetBundles-Building.html)

Output of the Build

[](AssetBundles-Cache.html)

AssetBundle compression and caching

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

