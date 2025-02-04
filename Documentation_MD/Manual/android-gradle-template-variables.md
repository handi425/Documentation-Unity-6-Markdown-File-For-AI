[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/android-gradle-template-variables.html)
  * [中文](/cn/current/Manual/android-gradle-template-variables.html)
  * [日本語](/ja/current/Manual/android-gradle-template-variables.html)
  * [한국어](/kr/current/Manual/android-gradle-template-variables.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/android-gradle-template-variables.html)
  * [中文](/cn/current/Manual/android-gradle-template-variables.html)
  * [日本語](/ja/current/Manual/android-gradle-template-variables.html)
  * [한국어](/kr/current/Manual/android-gradle-template-variables.html)

  * [Platform development ](PlatformSpecific.html)
  * [Android](android.html)
  * [Building and delivering for Android](android-building-and-delivering.html)
  * Gradle template variables

[](gradle-templates.html)

Gradle templates

[](android-modify-gradle-project-files.html)

Modify Gradle project files

# Gradle template variables

You can use the following variables in custom **Gradle** An Android build
system that automates several build processes. This automation means that many
common build errors are less likely to occur. [More info](android-gradle-
overview.html)  
See in [Glossary](Glossary.html#Gradle) template files:

**Variable** | **Description**  
---|---  
**ABIFILTERS** | Specifies the Application Binary Interfaces (ABIs) that your application should support. For example, `armeabi-v7a`, `arm64-v8a`. Gradle creates application builds for the specified `ABIFILTERS` values only.  
**APIVERSION** | The API version to build for. Unity sets the **APIVERSION** and **TARGETSDK** to the same value (**Target API Level** in the [Android Player Settings](class-PlayerSettingsAndroid.html)).  
**APPLICATIONID** | Android Application ID. For example, `com.mycompany.myapp`.  
**APPLY_PLUGINS** | Specifies a list of Gradle **plug-ins** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in) to use during the build process.  
**BUILDTOOLS** | The SDK build tools to use.  
**BUILD_SCRIPT_DEPS** | Specifies a list of dependencies and repositories required during the build process.  
**BUILTIN_NOCOMPRESS** | Specifies a default list of file extensions to exclude from **compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](class-TextureImporterOverride), [Animation Compression](class-AnimationClip.html#AssetProperties), [Audio Compression](class-AudioClip.html), [Build Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression). The file extensions are:
`.unity3d`, `.ress`, `.resource`, `.obb`, `.bundle`, `.unityexp`.  
**DEBUGSYMBOLLEVEL** | Indicates the type of symbols package that contains debug metadata required for debugging your application. You can set the values to **none** for no debug metadata, **symbol_table** for symbols package with only symbol tables, or **full** for symbols package with symbol tables and debugging information.  
**DEFAULT_CONFIG_SETUP** | Includes additional configuration components for `android.defaultConfig`.  
**DEPS** | The list of project dependencies. This is the list of libraries that the project uses.  
**DIR_GRADLEPROJECT** | The directory where Unity creates the Gradle project.  
**DIR_UNITYPROJECT** | The directory of your Unity project.  
**EXTERNAL_SOURCES** | The build script required to produce build artifacts such as, GameActivity and Swappy native libraries.  
**GOOGLE_PLAY_DEPENDENCIES** | Specifies the Google Play services your application requires. For example, `com.google.android.gms:play-services-ads:23.2.0`.  
**IL_CPP_BUILD_SETUP** | The build script required to produce build artifacts related to **IL2CPP** A Unity-developed scripting back-end which you can use as an alternative to Mono when building projects for some platforms. [More info](./scripting-backends-il2cpp.html)  
See in [Glossary](Glossary.html#IL2CPP), such as `libil2cpp.so`.  
**LAUNCHER_SOURCE_BUILD_SETUP** | Unity’s internal build script.  
**LIBSDKTARGET** | The target API level the Unity library supports.  
**MINIFY_DEBUG** | Indicates whether to minify debug builds.  
**MINIFY_RELEASE** | Indicates whether to minify release builds.  
**MINSDK** | The minimum API version that supports the application.  
**NAMESPACE** | The application namespace. For example, `com.MyCompany.MyApp`.  
**NDKPATH** | Specifies the Android Native Development Kit (NDK) installation folder path set in the **Android** section of **External Tools** , menu: **Edit** > **Preferences** > **External Tools** (macOS: **Unity** > **Settings** > **External Tools**).  
**NDKVERSION** | The Android NDK (Native Development Kit) version Unity is using. For example, `ndkVersion "20.0.5594570"`.  
**PACKAGING** | Specifies the required **APK** The Android Package format output by Unity. An APK is automatically deployed to your device when you select File > Build & Run. [More info](android-BuildProcess.html)  
See in [Glossary](Glossary.html#APK) packaging options.  
**PLAY_ASSET_PACKS** | Specifies the [asset packs](play-asset-delivery.html) to include in your application.  
**SIGN** | Complete the `signingConfigs` section if this build is signed.  
**SIGNCONFIG** | Indicates whether the build is signed. If this property is set to `signingConfig.release`, the build is signed.  
**SOURCE_BUILD_SETUP** | Unity’s internal build script.  
**SPLITS** | Indicates whether your application supports multiple APK builds.  
**SPLITS_VERSION_CODE** | Build script that sets version code for split APKs.  
**TARGETSDK** | The API version to target. Unity sets the and **APIVERSION** to the same value (**Target API Level** in the [Android Player Settings](class-PlayerSettingsAndroid.html)).  
**USER_PROGUARD** | Specifies a custom ProGuard file to use for minification.  
**VERSIONCODE** | The internal version number for the application. It’s used to indicate how recent the application version is, where higher number denotes a more recent version.  
**VERSIONNAME** | The application version number expressed as a string. This version number is visible to the users.  
  
Custom `settingsTemplate.gradle` files can also contain the following
variables:

**Variable** | **Description**  
---|---  
**INCLUDES** | The list of Android Library plug-ins to include in the Gradle project.  
**ARTIFACTORYREPOSITORY** | Adds a reference to Unity’s maven repository only for internal use. Unity deletes this during the build process.  
  
Custom `gradleTemplate.properties` files can also contain the following
variables:

**Variable** | **Description**  
---|---  
**ADDITIONAL_PROPERTIES** | Contains additional properties for the application. This includes:   
• The Gradle template version.  
• The path to the Unity project.  
• If the application uses the [Android App Bundle](android-
BuildProcess.html#publishing-format) publishing format, a flag that indicates
to keep native libraries compressed.  
• If the application uses the [GameActivity](android-application-entries-game-
activity.html) application entry point, a flag that indicates to use AndroidX.  
**JVM_HEAP_SIZE** | The maximum size of the [Java virtual machine (JVM) heap](https://www.ibm.com/docs/en/integration-bus/10.0?topic=development-jvm-heap-sizing).  
**STREAMING_ASSETS** | The list of files in the [Steaming Assets](StreamingAssets.html) folder that Gradle shouldn’t compress.  
  
## Additional resources

  * [Modify Gradle project files with Gradle template files](android-modify-gradle-project-files-templates.html)

[](gradle-templates.html)

Gradle templates

[](android-modify-gradle-project-files.html)

Modify Gradle project files

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

