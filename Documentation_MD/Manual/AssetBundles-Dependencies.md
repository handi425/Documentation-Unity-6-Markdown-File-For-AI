[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/AssetBundles-Dependencies.html)
  * [中文](/cn/current/Manual/AssetBundles-Dependencies.html)
  * [日本語](/ja/current/Manual/AssetBundles-Dependencies.html)
  * [한국어](/kr/current/Manual/AssetBundles-Dependencies.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/AssetBundles-Dependencies.html)
  * [中文](/cn/current/Manual/AssetBundles-Dependencies.html)
  * [日本語](/ja/current/Manual/AssetBundles-Dependencies.html)
  * [한국어](/kr/current/Manual/AssetBundles-Dependencies.html)

  * [Working in Unity](working-in-unity.html)
  * [Assets and media](assets-and-media.html)
  * [Asset workflow](AssetWorkflow.html)
  * [AssetBundles](AssetBundlesIntro.html)
  * AssetBundle Dependencies

[](AssetBundles-Preparing.html)

Preparing Assets for AssetBundles

[](AssetBundles-Building.html)

Output of the Build

# AssetBundle Dependencies

AssetBundles can become dependent on other AssetBundles if one or more of the
`UnityEngine.Objects` contains a reference to a `UnityEngine.Object` located
in another bundle. A dependency does not occur if the `UnityEngine.Object`
contains a reference to a `UnityEngine.Object` that is not contained in any
AssetBundle. In this case, a copy of the object that the bundle would be
dependent on is copied into the bundle when you build the AssetBundles. If
multiple objects in multiple bundles contain a reference to the same object
that isn’t assigned to a bundle, every bundle that would have a dependency on
that object will make its own copy of the object and package it into the built
AssetBundle.

Should an AssetBundle contain a dependency, it is important that the bundles
that contain those dependencies are loaded before the object you’re attempting
to instantiate is loaded. Unity will not attempt to automatically load
dependencies.

Consider the following example, a Material in **Bundle 1** references a
Texture in **Bundle 2** :

In this example, before loading the Material from **Bundle 1** , you would
need to load **Bundle 2** into memory. It does not matter which order you load
**Bundle 1** and **Bundle 2** , the important takeaway is that **Bundle 2** is
loaded before loading the Material from **Bundle 1**. In the section [Using
AssetBundles Natively](AssetBundles-Native.html) we’ll discuss how you can use
the `AssetBundleManifest` object that is produced by the build to determine,
and load, dependencies at runtime.

## Duplicated information across AssetBundles

By default, Unity doesn’t optimize duplicated information across AssetBundles.
This means multiple AssetBundles in your Project might contain the same
information, such as a Material which is used by multiple **Prefabs** An asset
type that allows you to store a GameObject complete with components and
properties. The prefab acts as a template from which you can create new object
instances in the scene. [More info](Prefabs.html)  
See in [Glossary](Glossary.html#Prefab). Assets which are used in multiple
AssetBundles are known as common Assets. These can affect memory resources and
loading times.

This page describes how Unity manages duplicated information across
AssetBundles, and how you can apply optimization.

### Editor setup

By default, Unity doesn’t perform any optimization to reduce or minimize the
memory required to store duplicate information. During build creation, Unity
builds duplicates of any implicitly referenced Assets inside the AssetBundles.
To prevent this duplication, assign common Assets (such as Materials) to their
own AssetBundle.

For example: you could have an application with two Prefabs, both of which are
assigned to their own AssetBundle. Both Prefabs share the same Material, which
is not assigned to an AssetBundle. This Material references a Texture, which
is not assigned to an AssetBundle.

If you follow the [AssetBundle Workflow](AssetBundles-Workflow.html) and use
the example class `CreateAssetBundles` to build AssetBundles, each generated
AssetBundle contains the Material (including its Shader and referenced
Textures). In the example image below, the Prefab files have a size of 383 KB
and 377 KB respectively.

![](../uploads/Main/AssetBundleDuplicate.png)

If the project contains a larger number of Prefabs, this behaviour impacts the
final installer size, and the runtime memory footprint when both AssetBundles
are loaded. Data duplication across AssetBundles also impacts batching,
because Unity considers each copy of the same Material as a unique Material.

To avoid data duplication, assign the Material and its referenced Assets to
its own `modulesmaterials` AssetBundle. You can also tag the Material only,
because the Texture dependency is also included in the AssetBundle
automatically during the build process.

Now if you rebuild the AssetBundles, the generated output includes a separate
`modulesmaterials` AssetBundle (359 KB), which contains the Material and its
associated Texture. This significantly reduces the size of the other
AssetBundles for the Prefabs (from roughly 380 KB in the previous iteration
down to roughly 20 KB).

The image below illustrates this.

![](../uploads/Main/AssetBundleSeparate.png)

### Runtime loading

When you extract common Assets to a single AssetBundle, be careful about
dependencies. In particular, if you only use a Prefab to instantiate a module,
the Materials do not load.

![A Prefab without a loaded Material](../uploads/Main/MaterialNotLoaded.png) A
Prefab without a loaded Material

To solve this problem, load the Materials AssetBundle in memory before you
load the AssetBundle that belongs to the module. In the following example,
this happens in the variable `materialsAB`.

    
    
    using System.IO;
    using UnityEngine;
    
    public class InstantiateAssetBundles : MonoBehaviour
    {
        void Start()
        {
            var materialsAB = AssetBundle.LoadFromFile(Path.Combine(Application.dataPath, Path.Combine("AssetBundles", "modulesmaterials")));
            var moduleAB = AssetBundle.LoadFromFile(Path.Combine(Application.dataPath, Path.Combine("AssetBundles", "example-prefab")));
    
            if (materialsAB == null || moduleAB == null)
            {
                Debug.Log("Failed to load AssetBundle!");
                return;
            }
            var prefab = moduleAB.LoadAsset<GameObject>("example-prefab");
            Instantiate(prefab);
        }
    }
    
    

![A Prefab with a correctly loaded
Material](../uploads/Main/MaterialLoaded.png) A Prefab with a correctly loaded
Material

**Note:** When you use LZ4 compressed and uncompressed AssetBundles,
[AssetBundle.LoadFromFile](../ScriptReference/AssetBundle.LoadFromFile.html)
only loads the catalog of its content in memory, but not the content itself.
To check if this is happening, use the [Memory
Profiler](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@0.2/manual/index.html)
package to [inspect memory
usage](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@0.2/manual/workflow-
memory-usage.html).

[](AssetBundles-Preparing.html)

Preparing Assets for AssetBundles

[](AssetBundles-Building.html)

Output of the Build

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

