[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/webgl-caching.html)
  * [中文](/cn/current/Manual/webgl-caching.html)
  * [日本語](/ja/current/Manual/webgl-caching.html)
  * [한국어](/kr/current/Manual/webgl-caching.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/webgl-caching.html)
  * [中文](/cn/current/Manual/webgl-caching.html)
  * [日本語](/ja/current/Manual/webgl-caching.html)
  * [한국어](/kr/current/Manual/webgl-caching.html)

  * [Platform development ](PlatformSpecific.html)
  * [Web](webgl.html)
  * [Web development](webgl-develop.html)
  * Cache behavior in Web

[](webgl-memory.html)

Memory in Unity Web

[](webgl-graphics.html)

Web graphics

# Cache behavior in Web

In the Unity Web platform, the **Cache API** A Javascript API to store network
request and response pairs in the browser cache. [More
info](https://developer.mozilla.org/en-US/docs/Web/API/Cache)  
See in [Glossary](Glossary.html#CacheAPI) lets you store the asset data cached
in `.data` files and [AssetBundles](AssetBundlesIntro.html) within the browser
cache. Storage limits for the browser cache such as maximum file size, maximum
overall cache size, and eviction criteria are dependent on the browser and
platform that you’re using. For more information, see [Browser storage limits
and eviction criteria](https://developer.mozilla.org/en-
US/docs/Web/API/IndexedDB_API/Browser_storage_limits_and_eviction_criteria).

## Data Caching

To access **Data Caching** , open the **Publishing Setings** for Web from
**File** > **Build Settings** > **Player Settings**. This enables the browser
to cache the main data files into the IndexedDB database.

Using the default browser HTTP cache doesn’t guarantee that the browser caches
a particular response. This is because the browser HTTP cache has limited
space, and the browser might not be able to cache files that are too large.

To improve your loading speed, `IndexedDB` allows you to cache files above the
browser limit. When you cache more files, you increase the chance that
downloaded content is available on the user’s machine during the next run of
the build.

Data Caching only caches the `.data` files in the IndexedDB cache for HTTP
responses. To cache [AssetBundles](AssetBundlesIntro.html), you need to enable
Data Caching and override `unityInstance.Module.cacheControl()`. To do this,
make sure `Module.cacheControl(url)` returns `must-revalidate` for the
requested AssetBundle URL. For example, you can override the
`unityInstance.Module.cacheControl()` function in the fulfillment callback of
the Promise that `createUnityInstance()` returns. For further information on
`createUnityInstance()`, see [Compressed builds and server
configuration](webgl-deploying.html).

## Customize Web Cache behavior

By default, the Web Cache stores the asset data file `.data` and AssetBundle
files `.bundle`, and revalidates them before loading them from the cache. You
can change this behavior by adding a new [Web template](webgl-templates.html)
that changes the UnityLoader configuration.

The following example shows adding a custom cacheControl function to the
UnityLoader configuration within the `index.html` file.

    
    
    var config = {
       // ...
    #if USE_DATA_CACHING
       cacheControl: function (url) {
         // Caching enabled for .data and .bundle files.
         // Revalidate if file is up to date before loading from cache
         if (url.match(/\.data/) || url.match(/\.bundle/)) {
             return "must-revalidate";
         }
    
         // Caching enabled for .mp4 and .custom files
         // Load file from cache without revalidation.
         if (url.match(/\.mp4/) || url.match(/\.custom/)) {
             return "immutable";
         }
    
         // Disable explicit caching for all other files.
         // Note: the default browser cache may cache them anyway.
         return "no-store";
       },
    #endif
       // ...
    }
    

The `cacheControl` function takes the url of a request as a parameter and
returns one of the following:

  * `must-revalidate` \- If the function returns [must-revalidate](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control#must-revalidate), the cache returns to an enabled state and the file is revalidated before being loaded from the cache.

  * `immutable` \- If the function returns [immutable](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control#immutable)You cannot change the contents of an immutable (read-only) package. This is the opposite of **mutable**. Most packages are immutable, including packages downloaded from the package registry or by Git URL.  
See in [Glossary](Glossary.html#Immutable), the cache is enabled and the file
is loaded from the cache without revalidation.

  * `no-store` \- If the function returns [no-store](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control#no-store), the cache is disabled.

The browser automatically stores (caches) certain file types such as .html,
.js, .css, .json, .jpg, .png, so they don’t need to be explicitly stored in
the Web Cache. Typical candidates for the Web cache include large files and
files that use a custom file format.

[](webgl-memory.html)

Memory in Unity Web

[](webgl-graphics.html)

Web graphics

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

