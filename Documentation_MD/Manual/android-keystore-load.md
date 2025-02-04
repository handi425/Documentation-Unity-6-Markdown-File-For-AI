[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/android-keystore-load.html)
  * [中文](/cn/current/Manual/android-keystore-load.html)
  * [日本語](/ja/current/Manual/android-keystore-load.html)
  * [한국어](/kr/current/Manual/android-keystore-load.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/android-keystore-load.html)
  * [中文](/cn/current/Manual/android-keystore-load.html)
  * [日本語](/ja/current/Manual/android-keystore-load.html)
  * [한국어](/kr/current/Manual/android-keystore-load.html)

  * [Platform development ](PlatformSpecific.html)
  * [Android](android.html)
  * [Getting started with Android](android-getting-started.html)
  * [Android keystores](android-keystore.html)
  * Load a keystore

[](android-keystore-add-keys.html)

Add keys to a keystore

[](android-developing.html)

Developing for Android

# Load a keystore

This page explains how to load an existing keystore and select a key from it
to use as the project key.

This is relevant if you want to publish your application, because you must
provide a key from a keystore when you sign the application.

To load an existing keystore:

  1. Open [Android Publishing Settings](class-PlayerSettingsAndroid.html#Publishing).
  2. Under the **Project Keystore** heading, enable **Custom Keystore**.
  3. Click the drop-down below **Custom Keystore**.
  4. Select **Browse** to load a keystore from your file system, or select a keystore from below the partition in the **UI**(User Interface) Allows a user to interact with your application. Unity currently supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI). The keystores below the partition are
those stored in the keystores dedicated location. For more information, see
[Choose the keystore location](android-keystore-create.html#choose-the-
keystore-location).

  5. Enter the password for the keystore in the **Password** property field. If the password is correct, Unity loads the keystore.

## Select a project key

After you load a keystore into your project, select a key from the keystore to
use as the project key. To do this:

  1. Open [Android Publishing Settings](class-PlayerSettingsAndroid.html#Publishing).
  2. Under the **Project Key** heading, set **Alias** to the key you want to use.
  3. In the **Password** property field, enter the password for the key.

## Additional resources

  * [Keystore Manager window reference](android-keystore-manager.html)
  * [Add keys to a keystore](android-keystore-add-keys.html)

[](android-keystore-add-keys.html)

Add keys to a keystore

[](android-developing.html)

Developing for Android

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

