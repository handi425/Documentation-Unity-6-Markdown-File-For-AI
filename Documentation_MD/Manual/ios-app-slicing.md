[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/ios-app-slicing.html)
  * [中文](/cn/current/Manual/ios-app-slicing.html)
  * [日本語](/ja/current/Manual/ios-app-slicing.html)
  * [한국어](/kr/current/Manual/ios-app-slicing.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/ios-app-slicing.html)
  * [中文](/cn/current/Manual/ios-app-slicing.html)
  * [日本語](/ja/current/Manual/ios-app-slicing.html)
  * [한국어](/kr/current/Manual/ios-app-slicing.html)

  * [Platform development ](PlatformSpecific.html)
  * [iOS](iphone.html)
  * [Building and delivering for iOS](ios-building-and-delivering.html)
  * [App thinning](AppThinning.html)
  * App slicing

[](ios-ondemand-resources.html)

On-demand resources

[](apple-privacy-manifest-policy.html)

Apple’s privacy manifest policy requirements

# App slicing

App slicing allows you to dynamically download Assets according to the
specification of the device the application is running on. For example, app
slicing can download high-resolution Assets for larger devices and low-
resolution Assets for smaller devices. App slicing works by defining
AssetBundles, with the added provision of variants. You can decide which
variant to use at startup and automatically append this to the Asset file name
upon download.

## Create a variant

To create a variant, use the following steps:

  1. Click on your [AssetBundle folder](ios-ondemand-resources.html#create-asset-bundle) and navigate to the Asset Labels section at the bottom of the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window.

  2. Click on the right-hand drop-down menu, select **New** , and enter the name of your new variants. AssetBundle variants must be lowercase.
  3. Create a new script in the Unity Editor folder called `BuildiOSAppSlices.cs`.
  4. Copy and paste the following code, replacing the example label `textures` and variants `hd` and `sd` with your own. In this code example, multiple folders are referenced: one containing HD textures and one containing SD textures. These folders have been given the variants **hd** and **sd**.

    
    
    using UnityEngine;
    using UnityEditor;
    
    
    public class BuildiOSAppSlices : MonoBehaviour
    {
        [InitializeOnLoadMethod]
        static void SetupResourcesBuild( )
        {
            UnityEditor.iOS.BuildPipeline.collectResources += CollectResources;
        }
    
        static UnityEditor.iOS.Resource[] CollectResources( )
        {
            return new UnityEditor.iOS.Resource[]
            {
                new UnityEditor.iOS.Resource("textures").BindVariant( "Assets/ODR/textures.hd", "hd" )
                                         .BindVariant( "Assets/ODR/textures.sd", "sd" )
                         .AddOnDemandResourceTags( "textures" ),
        };
        }
    
        [MenuItem( "Bundle/Build iOS App Slices" )]
        static void BuildAssetBundles( )
        {
            var options = BuildAssetBundleOptions.None;
    
            bool shouldCheckODR = EditorUserBuildSettings.activeBuildTarget == BuildTarget.iOS;
    
    #if UNITY_TVOS
                shouldCheckODR |= EditorUserBuildSettings.activeBuildTarget == BuildTarget.tvOS;
    #endif
    
            if( shouldCheckODR )
            {
    #if ENABLE_IOS_ON_DEMAND_RESOURCES
                if( PlayerSettings.iOS.useOnDemandResources )
                    options |= BuildAssetBundleOptions.UncompressedAssetBundle;
    #endif
    
    #if ENABLE_IOS_APP_SLICING
                options |= BuildAssetBundleOptions.UncompressedAssetBundle;
    #endif
            }
    
            BuildPipeline.BuildAssetBundles( "Assets/ODR", options, EditorUserBuildSettings.activeBuildTarget );
        }
    
    }
    

This code creates a new menu in the Unity Editor menu bar called **Bundle**.
Click this and select **Build iOS App Slices**. This generates the
AssetBundles in the `ODR` folder.

## Load an asset

To load an Asset, create a script file named `LoadBundle.cs` in your Assets
folder and copy in the following code. Replace `textures` with the name of the
variant you want to load.

    
    
    using UnityEngine;
    using UnityEngine.iOS;
    using System;
    using System.Collections;
    
    public class LoadBundle : MonoBehaviour
    {
        public AssetBundle     TextureBundle;
    
    
        void Start( )
        {
            LoadAssetAsync( "textures", "textures" );
        }
    
        public IEnumerator LoadAsset( string resourceName, string odrTag )
        {
            // Create the request
            using(OnDemandResourcesRequest request = OnDemandResources.PreloadAsync( new string[] { odrTag } ))
            {
                // Wait until request is completed
                await request;
    
                // Check for errors
                if( request.error != null )
                    throw new Exception( "ODR request failed: " + request.error );
    
                TextureBundle = AssetBundle.LoadFromFile( "res://" + resourceName );
    
            }
        }
    }
    

## Modify a variant

There might be times where you want to use a variant on a specific device, or
on devices that run over a set memory limit. To do this, you can change the
settings of each variant you use.

To modify a variant, navigate to **Player Settings** > **Other Settings** >
**Configuration** and expand **Variant map for app slicing**.

**Note** : Enable **Use on demand resources** in **Player Settings** >
**Other** > **Configuration** to view the **Variant map for app slicing**
options.

**Setting** | **Description**  
---|---  
**Variant name** | Displays the name of the variant from the loading script.  
**Device** | Choose which device this variant targets.  
**Memory** | Select the minimum memory required for this variant.  
**Graphics** | Choose the [Metal framework](https://developer.apple.com/documentation/metal) to use with this variant.  
**Display color space** | Select the color gamut to use with this variant.  
**Add custom entry** | Click **Add custom entry** to add your own custom settings and values.  
| **Key** | Enter the name of the setting.  
| **Value** | Enter the value for this setting.  
  
## Additional resources

  * [On-demand resources](ios-ondemand-resources.html)

[](ios-ondemand-resources.html)

On-demand resources

[](apple-privacy-manifest-policy.html)

Apple’s privacy manifest policy requirements

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

