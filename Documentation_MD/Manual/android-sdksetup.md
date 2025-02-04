[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/android-sdksetup.html)
  * [中文](/cn/current/Manual/android-sdksetup.html)
  * [日本語](/ja/current/Manual/android-sdksetup.html)
  * [한국어](/kr/current/Manual/android-sdksetup.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/android-sdksetup.html)
  * [中文](/cn/current/Manual/android-sdksetup.html)
  * [日本語](/ja/current/Manual/android-sdksetup.html)
  * [한국어](/kr/current/Manual/android-sdksetup.html)

  * [Platform development ](PlatformSpecific.html)
  * [Android](android.html)
  * [Getting started with Android](android-getting-started.html)
  * Android environment setup

[](android-getting-started.html)

Getting started with Android

[](class-PlayerSettingsAndroid.html)

Android Player settings

# Android environment setup

To create a Unity application for Android, you first need to set up your Unity
project to support Android. To support Android, a Unity project requires the
following dependencies:

  * The **Android Build Support** module.
  * The Android Software Development Kit [(SDK)](https://developer.android.com/studio#command-tools).
  * The Native Development Kit [(NDK)](https://developer.android.com/ndk/).
  * A Java Development Kit. By default, Unity uses [OpenJDK](http://openjdk.java.net/).

Before you get started, check Unity’s [Requirements and compatibility
documentation](android-requirements-and-compatibility.html) for Android to
make sure you’re aware of any limitations for developing a Unity application
for Android.

## Installing dependencies

Unity distributes dependencies as
[modules](https://docs.unity3d.com/hub/manual/AddModules.html) which means you
must use the [Unity Hub](https://docs.unity3d.com/hub/manual/index.html) to
install them. You can install them either when you install a new Unity Editor
version, or add them to an existing Unity Editor install. To install modules:

  * At install time, refer to [Downloading and installing Editors and modules with the Unity Hub](https://docs.unity3d.com/hub/manual/InstallEditors.html).
  * To an existing install, refer to [Add modules](https://docs.unity3d.com/hub/manual/AddModules.html).

The three modules to install are:

  * **Android Build Support**
  * **Android SDK & NDK Tools**
  * **OpenJDK**

![Unity Hub displaying the three dependency modules.](../uploads/Main/android-
modules.png) Unity Hub displaying the three dependency modules.

Unity installs **Android SDK & NDK Tools** and **OpenJDK** respectively in the
`SDK`, `NDK`, and `OpenJDK` folders under
`/[EditorVersion]/Editor/Data/PlaybackEngines/AndroidPlayer/`.

### Customizing dependencies

You should use the Unity Hub to install **Android SDK & NDK tools** and
**OpenJDK** to ensure that you receive the correct versions and
configurations. However, there are situations where it’s useful to change the
SDK, NDK, or JDK that Unity uses to build applications for Android. For
example, if you have multiple versions of Unity with the same dependencies and
you don’t want to duplicate the installation of the SDK, NDK, and JDK, you can
specify a shared location.

To make Unity use a custom version of a dependency:

  1. Download the custom version of the dependency.  
**Warning** : Unity only officially supports versions of the OpenJDK, SDK, or
NDK that it supplies through the Hub. For more information, refer to Supported
dependency versions.

  2. In Unity’s main menu, go to **Edit** > **Preferences** > **External Tools** > **Android** (macOS: **Unity** > **Settings** > **External Tools** > **Android**)
  3. Refer to the External tools for Android documentation to understand how to customize the installation of **JDK** , **SDK** , **NDK** , and ****Gradle** An Android build system that automates several build processes. This automation means that many common build errors are less likely to occur. [More info](android-gradle-overview.html)  
See in [Glossary](Glossary.html#Gradle)**.

#### Supported dependency versions

This section contains information on which versions of each dependency each
Unity version supports. Each version of Unity requires a specific version of
the Android NDK and Android JDK, but there are no exact version requirements
for the Android SDK.

##### SDK

Unity relies on tools that the Android SDK provides and different versions of
the SDK usually have the same tools available. This means you can use any
recent version of the SDK as they all contain the build tools that Unity
requires.

The following table shows the supported versions of Android SDK tools
installed with each Unity version:

**Unity version** | **SDK tools version** | **SDK Build tools version** | **SDK Command-line tools version** | **SDK Platform tools version**  
---|---|---|---|---  
6000.0 | 26.1.1 | 34.0.0 | 6 | 34.0.5  
2022.3 LTS | 26.1.1 | 32.0.0 | 6 | 32.0.0  
2021.3 LTS | 26.1.1 | 32.0.0 | 6 | 32.0.0  
2020.3 LTS | 26.1.1 | 30.0.2 | 2 | 28.0.1  
  
**Important** : Unity versions 2020.3 and 2021.3 LTS do not support Android
SDK Build tools versions 31 and above.

##### NDK

The following table shows the NDK version that each Unity version supports:

**Unity version** | **NDK version**  
---|---  
6000.0 | r23b (23.1.7779620)  
2022.3 LTS | r23b (23.1.7779620)  
2021.3 LTS | r21d (21.3.6528147)  
2020.3 LTS | r19 (19.0.5232133)  
  
##### JDK

The following table shows the JDK version that each Unity version supports:

**Unity version** | **JDK version**  
---|---  
6000.0 | 17 (OpenJDK version 17)  
2022.3 LTS | 11 (OpenJDK version 11)  
2021.3 LTS | 11 (OpenJDK version 11)  
2020.3 LTS | 8 (OpenJDK version 1.8)  
  
**Note** : Only Unity version 2023.2 supports CMake version 3.22.1. Unity
versions 2022.3 and below do not support CMake.

## External Tools for Android

The **External Tools** section for Android allows you to configure settings
for Android development tools used to set up Unity projects on Android
devices. To access the **External Tools** section for Android, go to **Edit**
> **Preferences** (macOS: **Unity** > **Settings**) and then navigate to
**External Tools** > **Android**.

For general **Preferences** settings, refer to
[Preferences](Preferences.html).

![External Tools for Android](../uploads/Main/PreferenceesExternalToolsAndroid.png) External Tools for Android **Setting** | **Description**  
---|---  
**JDK installed with Unity(recommended)** | Indicates whether to use the recommended version of Java Development Kit (JDK) installed with Unity or the custom JDK installation. If enabled, the setting displays the path to the JDK installation folder. To use the custom JDK version, disable this option and click **Browse** to set the custom JDK installation folder path.  
**Android SDK tools installed with Unity(recommended)** | Indicates whether to use the recommended versions of Android SDK tools installed with Unity or the custom SDK tools installation. If enabled, the setting displays the path to the SDK tools installation folder. To use the custom SDK tools version, disable this option and click **Browse** to set the custom SDK tools installation folder path.  
**Android NDK installed with Unity(recommended)** | Indicates whether to use the recommended version of Android Native Development Kit (NDK) installed with Unity or the custom NDK installation. If enabled, the setting displays the path to the NDK installation folder. To use the custom NDK version, disable this option and click **Browse** to set the custom NDK installation folder path.  
**Gradle installed with Unity(recommended)** | Indicates whether to use the recommended version of Android Gradle installed with Unity or the custom Gradle installation. If enabled, the setting displays the path to the Gradle installation folder. To use the custom Gradle version, disable this option and click **Browse** to set the custom Gradle installation folder path.  
**Stop Gradle daemons on exit** | Indicates whether to stop Gradle daemons when the Unity Editor exits. This option is enabled by default and it might help to free up resources on your computer.  
**Kill**ADB** An Android Debug Bridge (ADB). You can use an ADB to deploy an
Android package (APK) manually after building. [More
info](https://developer.android.com/studio/command-line/adb.html)  
See in [Glossary](Glossary.html#ADB) server on exit** | Indicates whether to terminate Android Debug Bridge (adb) server when the Unity Editor exits. This option is enabled by default and it might help to free up resources on your computer.  
**Kill external ADB instances** | Indicates whether to terminate external Android Debug Bridge (ADB) instances. These are separate instances that don’t belong to the Android SDK set from **Android SDK tools installed with Unity(recommended)** . Multiple ADB instances can conflict with each other and might cause issues when using the Android SDK. For example, when updating the API or during application launches.   
  
**Note** : This option is enabled by default to prevent collision between
different ADB instances.  
**Maximum JVM heap size, Mbyte** | Specifies the maximum Java heap size that can be allocated during the Android build process. The value is specified in megabytes and the default value is 4096. You can increase or decrease this value based on your project requirement. Increase this value if you experience heap space errors.  
**Keystores Dedicated Location** | Specifies the folder path to your **Android keystores** An Android system that lets you store cryptographic key entries for enhanced device security. [More info](class-PlayerSettingsAndroid.html#projectkeystore)  
See in [Glossary](Glossary.html#AndroidKeystore). Unity uses this path when
signing your Android application during the build process. To set a new path
for your application, click **Browse** and navigate to the folder where you
want to store your Android keystores. For more information, refer to [Choose
the keystore location](android-keystore-create.html#choose-the-keystore-
location).  
  
## Setting the Android SDK Target API

The Unity Hub installs the latest version of the Android SDK Target API that
Google Play requires. If you need to use a more recent version, you can change
it in the [Android Player Settings](class-PlayerSettingsAndroid.html). To do
this:

  1. Select **Edit** > **Project Settings**.
  2. In the Project settings window, select the **Player** tab, then open [Android Player Settings](class-PlayerSettingsAndroid.html):  
![Selecting a target API for the Android SDK](../uploads/Main/android-player-
settings-tab.png)

  3. In the **Other Settings** section, change the **Target API Level**.  
![](../uploads/Main/android-sdk-target-api.png)

If you select a target API version newer than the latest installed version,
the Unity Android SDK Updater can automatically download and install the new
version. Unity displays a prompt and you can choose to either:

  * Automatically download and install the new version of the Android SDK.
  * Continue to use the highest installed version of the Android SDK.

If you select a target API version that isn’t installed and is older than the
latest installed version, the Unity Android SDK Updater can’t perform the
update and Unity displays an error message. In this case, to update the
Android SDK Target API, you must use the Android
[sdkmanager](https://developer.android.com/studio/command-line/sdkmanager)
from either [Android Studio](https://developer.android.com/studio) or the
[command-line tool](https://developer.android.com/studio/command-
line/sdkmanager). Regardless of the method you choose, make sure to select the
correct Android SDK folder for Unity in the **Edit** > **Preferences** >
**External Tools** window. For more information, refer to Customizing
dependencies.

**Important** : On Windows, if you installed the Unity Editor in the default
folder (`/Program Files/`), you must run the `sdkmanager` with elevated
privileges (**Run as Administrator**) to perform the update.

[](android-getting-started.html)

Getting started with Android

[](class-PlayerSettingsAndroid.html)

Android Player settings

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

