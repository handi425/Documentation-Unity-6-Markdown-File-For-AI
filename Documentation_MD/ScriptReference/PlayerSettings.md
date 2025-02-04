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

# PlayerSettings

class in UnityEditor

/

Inherits from:[Object](Object.html)

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

[Switch to Manual](../Manual/class-PlayerSettings.html "Go to PlayerSettings
Component in the Manual")

### Description

Player Settings is where you define various parameters for the final game that
you will build in Unity. Some of these values are used in the Resolution
Dialog that launches when you open a standalone game.

### Static Properties

[accelerometerFrequency](PlayerSettings-accelerometerFrequency.html)|
Accelerometer update frequency.  
---|---  
[actionOnDotNetUnhandledException](PlayerSettings-
actionOnDotNetUnhandledException.html)| Sets the crash behavior on .NET
unhandled exception.  
[advancedLicense](PlayerSettings-advancedLicense.html)| Is the advanced
version being used?  
[allowedAutorotateToLandscapeLeft](PlayerSettings-
allowedAutorotateToLandscapeLeft.html)| Is auto-rotation to landscape left
supported?  
[allowedAutorotateToLandscapeRight](PlayerSettings-
allowedAutorotateToLandscapeRight.html)| Is auto-rotation to landscape right
supported?  
[allowedAutorotateToPortrait](PlayerSettings-
allowedAutorotateToPortrait.html)| Is auto-rotation to portrait supported?  
[allowedAutorotateToPortraitUpsideDown](PlayerSettings-
allowedAutorotateToPortraitUpsideDown.html)| Is auto-rotation to portrait
upside-down supported?  
[allowFullscreenSwitch](PlayerSettings-allowFullscreenSwitch.html)| If
enabled, allows the user to switch between full screen and windowed mode using
OS specific keyboard short cuts.  
[allowHDRDisplaySupport](PlayerSettings-allowHDRDisplaySupport.html)| Prepare
the application to encode images for an HDR display.  
[allowUnsafeCode](PlayerSettings-allowUnsafeCode.html)| Allow unsafe C# code
to be compiled for predefined assemblies.  
[applicationIdentifier](PlayerSettings-applicationIdentifier.html)| The
application identifier for the currently selected build target.  
[bakeCollisionMeshes](PlayerSettings-bakeCollisionMeshes.html)| Pre bake
collision meshes on player build.  
[bundleVersion](PlayerSettings-bundleVersion.html)| Application bundle version
shared between iOS & Android platforms.  
[colorSpace](PlayerSettings-colorSpace.html)| Set the rendering color space
for the current project.  
[companyName](PlayerSettings-companyName.html)| The name of your company.  
[cursorHotspot](PlayerSettings-cursorHotspot.html)| Default cursor's click
position in pixels from the top left corner of the cursor image.  
[dedicatedServerOptimizations](PlayerSettings-
dedicatedServerOptimizations.html)| Performs additional optimizations on
Dedicated Server builds.  
[defaultCursor](PlayerSettings-defaultCursor.html)| The default cursor for
your application.  
[defaultInterfaceOrientation](PlayerSettings-
defaultInterfaceOrientation.html)| Default screen orientation for mobiles.  
[defaultScreenHeight](PlayerSettings-defaultScreenHeight.html)| Default
vertical dimension of stand-alone player window.  
[defaultScreenWidth](PlayerSettings-defaultScreenWidth.html)| Default
horizontal dimension of stand-alone player window.  
[defaultWebScreenHeight](PlayerSettings-defaultWebScreenHeight.html)| Default
vertical dimension of web player window.  
[defaultWebScreenWidth](PlayerSettings-defaultWebScreenWidth.html)| Default
horizontal dimension of web player window.  
[enable360StereoCapture](PlayerSettings-enable360StereoCapture.html)| Enable
360 Stereo Capture support on the current build target.  
[enableCrashReportAPI](PlayerSettings-enableCrashReportAPI.html)| Enables
CrashReport API.  
[enableFrameTimingStats](PlayerSettings-enableFrameTimingStats.html)| Enable
frame timing statistics.  
[enableInternalProfiler](PlayerSettings-enableInternalProfiler.html)| Enables
internal profiler.  
[enableMetalAPIValidation](PlayerSettings-enableMetalAPIValidation.html)|
Enables Metal API validation in the Editor.  
[enableOpenGLProfilerGPURecorders](PlayerSettings-
enableOpenGLProfilerGPURecorders.html)| Enable ProfilerRecorder usage to
record GPU timings when rendering with OpenGL.  
[forceSingleInstance](PlayerSettings-forceSingleInstance.html)| Restrict
standalone players to a single concurrent running instance.  
[fullScreenMode](PlayerSettings-fullScreenMode.html)| Platform agnostic
setting to define fullscreen behavior. Not all platforms support all modes.  
[gcIncremental](PlayerSettings-gcIncremental.html)| Allows you to enable or
disable incremental mode for garbage collection.  
[gpuSkinning](PlayerSettings-gpuSkinning.html)| Marked for deprecation in the
future. Use PlayerSettings.meshDeformation instead.  
[graphicsJobMode](PlayerSettings-graphicsJobMode.html)| Selects the graphics
job mode to use on platforms that support Native, Legacy and Split graphics
jobs.  
[graphicsJobs](PlayerSettings-graphicsJobs.html)| Enable graphics jobs (multi
threaded rendering).  
[hdrBitDepth](PlayerSettings-hdrBitDepth.html)| The number of bits in each
color channel for swap chain buffers.  
[insecureHttpOption](PlayerSettings-insecureHttpOption.html)| Determines if
plain text HTTP connections are allowed.  
[legacyClampBlendShapeWeights](PlayerSettings-
legacyClampBlendShapeWeights.html)| Defines whether the BlendShape weight
range in SkinnedMeshRenderers is clamped.  
[logObjCUncaughtExceptions](PlayerSettings-logObjCUncaughtExceptions.html)|
Are ObjC uncaught exceptions logged?  
[macRetinaSupport](PlayerSettings-macRetinaSupport.html)| Enable Retina
support for macOS.  
[meshDeformation](PlayerSettings-meshDeformation.html)| Specifies which method
Unity uses to process mesh deformations for skinning.  
[mipStripping](PlayerSettings-mipStripping.html)| Enable mip stripping for all
platforms.  
[MTRendering](PlayerSettings.MTRendering.html)| Is multi-threaded rendering
enabled?  
[muteOtherAudioSources](PlayerSettings-muteOtherAudioSources.html)| Stops or
allows audio from other applications to play in the background while your
Unity application is running.  
[openGLRequireES31](PlayerSettings-openGLRequireES31.html)| Specifies whether
the application requires OpenGL ES 3.1 support.  
[openGLRequireES31AEP](PlayerSettings-openGLRequireES31AEP.html)| Specifies
whether the application requires OpenGL ES 3.1 AEP support.  
[openGLRequireES32](PlayerSettings-openGLRequireES32.html)| Specifies whether
the application requires OpenGL ES 3.2 support.  
[preserveFramebufferAlpha](PlayerSettings-preserveFramebufferAlpha.html)| When
enabled, preserves the alpha value in the framebuffer to support rendering
over native UI on Android.  
[productName](PlayerSettings-productName.html)| The name of your product.  
[resetResolutionOnWindowResize](PlayerSettings-
resetResolutionOnWindowResize.html)| Indicates whether to reset the
application's screen resolution when the native window size changes.  
[resizableWindow](PlayerSettings-resizableWindow.html)| Use resizable window
in standalone player builds.  
[runInBackground](PlayerSettings-runInBackground.html)| If enabled, your game
will continue to run after lost focus.  
[spriteBatchVertexThreshold](PlayerSettings-spriteBatchVertexThreshold.html)|
Specifies the max vertex limit for Sprite batching.  
[statusBarHidden](PlayerSettings-statusBarHidden.html)| Returns if status bar
should be hidden. Supported on iOS only; on Android, the status bar is always
hidden.  
[stereoRenderingPath](PlayerSettings-stereoRenderingPath.html)| Active stereo
rendering path  
[strictShaderVariantMatching](PlayerSettings-
strictShaderVariantMatching.html)| Enable strict shader variant matching in
the player.  
[stripEngineCode](PlayerSettings-stripEngineCode.html)| Remove unused Engine
code from your build (IL2CPP-only).  
[stripUnusedMeshComponents](PlayerSettings-stripUnusedMeshComponents.html)|
Should unused Mesh components be excluded from game build?  
[suppressCommonWarnings](PlayerSettings-suppressCommonWarnings.html)|
Suppresses common C# warnings.  
[tvOSBundleVersion](PlayerSettings-tvOSBundleVersion.html)| Application bundle
version for the TVOS platform.  
[use32BitDisplayBuffer](PlayerSettings-use32BitDisplayBuffer.html)| 32-bit
Display Buffer is used.  
[useAnimatedAutorotation](PlayerSettings-useAnimatedAutorotation.html)| Let
the OS autorotate the screen as the device orientation changes.  
[useFlipModelSwapchain](PlayerSettings-useFlipModelSwapchain.html)| Use DXGI
flip model swap chain for D3D11.  
[useHDRDisplay](PlayerSettings-useHDRDisplay.html)| Switch the main display to
HDR mode (if available).  
[useMacAppStoreValidation](PlayerSettings-useMacAppStoreValidation.html)|
Enable receipt validation for the Mac App Store.  
[usePlayerLog](PlayerSettings-usePlayerLog.html)| Write a log file with
debugging information.  
[virtualRealitySplashScreen](PlayerSettings-virtualRealitySplashScreen.html)|
Virtual Reality specific splash screen.  
[visibleInBackground](PlayerSettings-visibleInBackground.html)| On Windows,
shows the application in the background if the Fullscreen Windowed mode is
used.  
[visionOSBundleVersion](PlayerSettings-visionOSBundleVersion.html)|
Application bundle version for the VisionOS platform.  
[vulkanEnableLateAcquireNextImage](PlayerSettings-
vulkanEnableLateAcquireNextImage.html)| Delays acquiring the swapchain image
until after the frame is rendered.  
[vulkanEnablePreTransform](PlayerSettings-vulkanEnablePreTransform.html)|
Applies the display rotation during rendering.  
[vulkanEnableSetSRGBWrite](PlayerSettings-vulkanEnableSetSRGBWrite.html)|
Enables Graphics.SetSRGBWrite() on Vulkan renderer.  
[vulkanNumSwapchainBuffers](PlayerSettings-vulkanNumSwapchainBuffers.html)|
Set number of swapchain buffers to be used with Vulkan renderer  
[windowsGamepadBackendHint](PlayerSettings-windowsGamepadBackendHint.html)|
Specifies the desired Windows API to be used for input.  
  
### Static Methods

[GetAdditionalCompilerArguments](PlayerSettings.GetAdditionalCompilerArguments.html)|
Gets an array of additional compiler arguments set for a specific
NamedBuildTarget.  
---|---  
[GetAdditionalIl2CppArgs](PlayerSettings.GetAdditionalIl2CppArgs.html)| Obtain
the additional arguments passed to the IL2CPP compiler during the player build
process.  
[GetApiCompatibilityLevel](PlayerSettings.GetApiCompatibilityLevel.html)| Gets
.NET API compatibility level for specified build target.  
[GetApplicationIdentifier](PlayerSettings.GetApplicationIdentifier.html)| Get
the application identifier for the specified platform.  
[GetArchitecture](PlayerSettings.GetArchitecture.html)| Gets the architecture
for the given build target.  
[GetCaptureStartupLogs](PlayerSettings.GetCaptureStartupLogs.html)| Returns
whether a given build target is configured to capture startuplogs  
[GetDefaultScriptingBackend](PlayerSettings.GetDefaultScriptingBackend.html)|
Returns the default ScriptingImplementation for the build target you select.  
[GetDefaultShaderChunkCount](PlayerSettings.GetDefaultShaderChunkCount.html)|
Gets the default limit on the number of shader variant chunks Unity loads and
keeps in memory.  
[GetDefaultShaderChunkSizeInMB](PlayerSettings.GetDefaultShaderChunkSizeInMB.html)|
Gets the default size for compressed shader variant chunks.  
[GetDynamicBatchingForPlatform](PlayerSettings.GetDynamicBatchingForPlatform.html)|
Returns true if dynamic batching is enabled for the given BuildTarget.  
[GetEditorAssembliesCompatibilityLevel](PlayerSettings.GetEditorAssembliesCompatibilityLevel.html)|
Gets .NET API compatibility level for the editor assemblies.  
[GetGraphicsAPIs](PlayerSettings.GetGraphicsAPIs.html)| Get graphics APIs to
be used on a build platform.  
[GetIcons](PlayerSettings.GetIcons.html)| Returns the list of assigned icons
for the specified build target.  
[GetIconSizes](PlayerSettings.GetIconSizes.html)| Returns a list of icon sizes
for the specified platform.  
[GetIl2CppCodeGeneration](PlayerSettings.GetIl2CppCodeGeneration.html)| Gets
the value of code generation option for IL2CPP.  
[GetIl2CppCompilerConfiguration](PlayerSettings.GetIl2CppCompilerConfiguration.html)|
Gets compiler configuration used when compiling generated C++ code for the
build target you specify.  
[GetIl2CppStacktraceInformation](PlayerSettings.GetIl2CppStacktraceInformation.html)|
Gets stack trace information option for il2cpp builds for the build target you
specify.  
[GetManagedStrippingLevel](PlayerSettings.GetManagedStrippingLevel.html)| Gets
the managed code stripping level set for the build target you select  
[GetMobileMTRendering](PlayerSettings.GetMobileMTRendering.html)| Check if
multithreaded rendering option for mobile platform is enabled.  
[GetNormalMapEncoding](PlayerSettings.GetNormalMapEncoding.html)| Gets the
NormalMapEncoding for the build target you select.  
[GetOverrideShaderChunkSettingsForPlatform](PlayerSettings.GetOverrideShaderChunkSettingsForPlatform.html)|
If the value is true, settings for the buildTarget override the default
settings.  
[GetPlatformIcons](PlayerSettings.GetPlatformIcons.html)| Gets the list of
available icon slots for the specified build target and kind.  
[GetPreloadedAssets](PlayerSettings.GetPreloadedAssets.html)| Returns the
assets that will be loaded at start up in the player and be kept alive until
the player terminates.  
[GetScriptingBackend](PlayerSettings.GetScriptingBackend.html)| Gets the
scripting framework for the build target you select.  
[GetScriptingDefineSymbols](PlayerSettings.GetScriptingDefineSymbols.html)|
Gets the user-specified symbols for script compilation for the build target
you select.  
[GetShaderChunkCountForPlatform](PlayerSettings.GetShaderChunkCountForPlatform.html)|
Gets the default limit on the number of shader variant chunks Unity loads and
keeps in memory for the build target.  
[GetShaderChunkSizeInMBForPlatform](PlayerSettings.GetShaderChunkSizeInMBForPlatform.html)|
Gets the default size for compressed shader variant chunks for the build
target.  
[GetShaderPrecisionModel](PlayerSettings.GetShaderPrecisionModel.html)| Gets
the active shader precision model.  
[GetStackTraceLogType](PlayerSettings.GetStackTraceLogType.html)| Gets stack
trace logging options.  
[GetStaticBatchingForPlatform](PlayerSettings.GetStaticBatchingForPlatform.html)|
Returns true if static batching is enabled for the given BuildTarget.  
[GetSupportedIconKinds](PlayerSettings.GetSupportedIconKinds.html)| Retrieves
all icon kinds that the specified build target supports  
[GetTemplateCustomValue](PlayerSettings.GetTemplateCustomValue.html)| Returns
a value of a custom template variable.  
[GetUseDefaultGraphicsAPIs](PlayerSettings.GetUseDefaultGraphicsAPIs.html)| Is
a build platform using automatic graphics API choice?  
[GetVirtualTexturingSupportEnabled](PlayerSettings.GetVirtualTexturingSupportEnabled.html)|
Is virtual texturing enabled.  
[SetAdditionalCompilerArguments](PlayerSettings.SetAdditionalCompilerArguments.html)|
Sets additional compiler arguments for a build target.  
[SetAdditionalIl2CppArgs](PlayerSettings.SetAdditionalIl2CppArgs.html)| Set
additional arguments passed to the IL2CPP compiler during the build process.  
[SetApiCompatibilityLevel](PlayerSettings.SetApiCompatibilityLevel.html)| Sets
.NET API compatibility level for specified build target.  
[SetApplicationIdentifier](PlayerSettings.SetApplicationIdentifier.html)| Set
the application identifier for the specified platform.  
[SetArchitecture](PlayerSettings.SetArchitecture.html)| Sets the architecture
for the given build target.  
[SetCaptureStartupLogs](PlayerSettings.SetCaptureStartupLogs.html)| Set
whether a given build target is configured to capture startuplogs  
[SetDefaultShaderChunkCount](PlayerSettings.SetDefaultShaderChunkCount.html)|
Sets the default limit on the number of shader variant chunks Unity loads and
keeps in memory.  
[SetDefaultShaderChunkSizeInMB](PlayerSettings.SetDefaultShaderChunkSizeInMB.html)|
Sets the default size for compressed shader variant chunks.  
[SetDynamicBatchingForPlatform](PlayerSettings.SetDynamicBatchingForPlatform.html)|
Sets dynamic batching for the given BuildTarget.  
[SetEditorAssembliesCompatibilityLevel](PlayerSettings.SetEditorAssembliesCompatibilityLevel.html)|
Sets .NET API compatibility level for Editor Assemblies.  
[SetGraphicsAPIs](PlayerSettings.SetGraphicsAPIs.html)| Sets the graphics APIs
used on a build platform.  
[SetIcons](PlayerSettings.SetIcons.html)| Assigns a list of icons for the
specified platform.  
[SetIl2CppCodeGeneration](PlayerSettings.SetIl2CppCodeGeneration.html)| Sets
the code generation option for IL2CPP for the specified build target.  
[SetIl2CppCompilerConfiguration](PlayerSettings.SetIl2CppCompilerConfiguration.html)|
Sets compiler configuration used when compiling generated C++ code for a
particular build target.  
[SetIl2CppStacktraceInformation](PlayerSettings.SetIl2CppStacktraceInformation.html)|
Sets stack trace information option for il2cpp builds for the build target you
specify.  
[SetManagedStrippingLevel](PlayerSettings.SetManagedStrippingLevel.html)| Sets
the managed code stripping level for specified build target.  
[SetMobileMTRendering](PlayerSettings.SetMobileMTRendering.html)| Enable or
disable multithreaded rendering option for mobile platform.  
[SetNormalMapEncoding](PlayerSettings.SetNormalMapEncoding.html)| Sets the
normal map encoding for the given build target.  
[SetOverrideShaderChunkSettingsForPlatform](PlayerSettings.SetOverrideShaderChunkSettingsForPlatform.html)|
Enable this to override the default shader variant chunk settings.  
[SetPlatformIcons](PlayerSettings.SetPlatformIcons.html)| Assign a list of
icons for the specified platform and icon kind.  
[SetPreloadedAssets](PlayerSettings.SetPreloadedAssets.html)| Assigns the
assets that will be loaded at start up in the player and be kept alive until
the player terminates.  
[SetScriptingBackend](PlayerSettings.SetScriptingBackend.html)| Sets the
scripting framework for a given build target.  
[SetScriptingDefineSymbols](PlayerSettings.SetScriptingDefineSymbols.html)|
Set user-specified symbols for script compilation for the given build target.  
[SetShaderChunkCountForPlatform](PlayerSettings.SetShaderChunkCountForPlatform.html)|
Sets the default limit on the number of shader variant chunks Unity loads and
keeps in memory on the build target.  
[SetShaderChunkSizeInMBForPlatform](PlayerSettings.SetShaderChunkSizeInMBForPlatform.html)|
Sets the default size for compressed shader variant chunks on the build
target.  
[SetShaderPrecisionModel](PlayerSettings.SetShaderPrecisionModel.html)| Sets
the shader precision model.  
[SetStackTraceLogType](PlayerSettings.SetStackTraceLogType.html)| Set stack
trace logging options. Note: calling this function will implicitly call
Application.SetStackTraceLogType.  
[SetStaticBatchingForPlatform](PlayerSettings.SetStaticBatchingForPlatform.html)|
Sets static batching for the given BuildTarget.  
[SetTemplateCustomValue](PlayerSettings.SetTemplateCustomValue.html)| Sets a
value of a custom template variable.  
[SetUseDefaultGraphicsAPIs](PlayerSettings.SetUseDefaultGraphicsAPIs.html)|
Should a build platform use automatic graphics API choice.  
[SetVirtualTexturingSupportEnabled](PlayerSettings.SetVirtualTexturingSupportEnabled.html)|
Enable virtual texturing.  
  
### Inherited Members

### Properties

[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
---|---  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
---|---  
[ToString](Object.ToString.html)| Returns the name of the object.  
  
### Static Methods

[Destroy](Object.Destroy.html)| Removes a GameObject, component or asset.  
---|---  
[DestroyImmediate](Object.DestroyImmediate.html)| Destroys the object obj
immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](Object.DontDestroyOnLoad.html)| Do not destroy the target
Object when loading a new Scene.  
[FindAnyObjectByType](Object.FindAnyObjectByType.html)| Retrieves any active
loaded object of Type type.  
[FindFirstObjectByType](Object.FindFirstObjectByType.html)| Retrieves the
first active loaded object of Type type.  
[FindObjectsByType](Object.FindObjectsByType.html)| Retrieves a list of all
loaded objects of Type type.  
[Instantiate](Object.Instantiate.html)| Clones the object original and returns
the clone.  
[InstantiateAsync](Object.InstantiateAsync.html)| Captures a snapshot of the
original object (that must be related to some GameObject) and returns the
AsyncInstantiateOperation.  
  
### Operators

[bool](Object-operator_Object.html)| Does the object exist?  
---|---  
[operator !=](Object-operator_ne.html)| Compares if two objects refer to a
different object.  
[operator ==](Object-operator_eq.html)| Compares two object references to see
if they refer to the same object.  
  
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

