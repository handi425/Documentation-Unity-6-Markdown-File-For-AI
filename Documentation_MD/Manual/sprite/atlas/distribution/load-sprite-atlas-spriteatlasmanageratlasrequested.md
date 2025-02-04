[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/sprite/atlas/distribution/load-sprite-atlas-spriteatlasmanageratlasrequested.html)
  * [中文](/cn/current/Manual/sprite/atlas/distribution/load-sprite-atlas-spriteatlasmanageratlasrequested.html)
  * [日本語](/ja/current/Manual/sprite/atlas/distribution/load-sprite-atlas-spriteatlasmanageratlasrequested.html)
  * [한국어](/kr/current/Manual/sprite/atlas/distribution/load-sprite-atlas-spriteatlasmanageratlasrequested.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/sprite/atlas/distribution/load-sprite-atlas-spriteatlasmanageratlasrequested.html)
  * [中文](/cn/current/Manual/sprite/atlas/distribution/load-sprite-atlas-spriteatlasmanageratlasrequested.html)
  * [日本語](/ja/current/Manual/sprite/atlas/distribution/load-sprite-atlas-spriteatlasmanageratlasrequested.html)
  * [한국어](/kr/current/Manual/sprite/atlas/distribution/load-sprite-atlas-spriteatlasmanageratlasrequested.html)

  * [Working in Unity](../../../working-in-unity.html)
  * [2D in Unity](../../../Unity2D.html)
  * [Sprites](../../../sprite/sprite-landing.html)
  * [Sprite atlas](../../../sprite/atlas/atlas-landing.html)
  * [Distribution](../../../sprite/atlas/distribution/distribution-landing.html)
  * Load a Sprite Atlas with SpriteAtlasManager.atlasRequested

[](../../../sprite/atlas/distribution/late-binding.html)

Late binding

[](../../../sprite/atlas/distribution/retrieve-sprite-contents-runtime-
getsprites.html)

Retrieve sprite contents at runtime with GetSprites

# Load a Sprite Atlas with SpriteAtlasManager.atlasRequested

`atlasRequested` is a callback that tells you when a **sprite** A 2D graphic
objects. If you are used to working in 3D, Sprites are essentially just
standard textures but there are special techniques for combining and managing
sprite textures for efficiency and convenience during development. [More
info](../../../sprite/sprite-landing.html)  
See in [Glossary](../../../Glossary.html#Sprite), which isn’t included in the
build, is requested. You need to manually load the **Sprite Atlas** A utility
that packs several sprite textures tightly together within a single texture
known as an atlas. [More info](../../../sprite/atlas/v2/v2-landing.html)  
See in [Glossary](../../../Glossary.html#SpriteAtlas) with late binding, and
send the sprite to the Unity Editor.

The following example demonstrates how to set up the callback to load the
[Sprite Atlas from an AssetBundle](../distribution/methods-distribution.html)
with late binding. Note that this script is for loading and binding a Sprite
Atlas to sprites which already exist in the build or project. You can create
sprites that don’t exist in the project from a Sprite Atlas by [retrieving the
Sprite Atlas’ contents at runtime with `GetSprites`](../distribution/retrieve-
sprite-contents-runtime-getsprites.html)

    
    
    void OnEnable()
    {
        SpriteAtlasManager.atlasRequested += RequestAtlas;
    }
    void OnDisable()
    {
        SpriteAtlasManager.atlasRequested -= RequestAtlas;
    }
    void RequestAtlas(string tag, System.Action callback)
    {
        if (spriteAtlas == null)
        {
            StartCoroutine(LoadFromStreammingAsset(callback));
        }
        else
        {
            callback(spriteAtlas);
        }
    }
    
    IEnumerator LoadFromStreammingAsset(System.Action callback)
    {
        string path = Application.streamingAssetsPath + "/" + bundleName;
        print(path);
        AssetBundleCreateRequest bundleLoadRequest = AssetBundle.LoadFromFileAsync(Application.streamingAssetsPath + "/" + bundleName);
        yield return bundleLoadRequest;
        bundle = bundleLoadRequest.assetBundle;
        if (bundle == null)
        {
            Debug.Log("Failed to load AssetBundle!");
            yield break;
        }
        SpriteAtlas spriteAtlas = bundle.LoadAsset(bundleName);
        callback(spriteAtlas);
    }
    

[](../../../sprite/atlas/distribution/late-binding.html)

Late binding

[](../../../sprite/atlas/distribution/retrieve-sprite-contents-runtime-
getsprites.html)

Retrieve sprite contents at runtime with GetSprites

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

