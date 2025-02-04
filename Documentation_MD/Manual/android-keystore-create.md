[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/android-keystore-create.html)
  * [中文](/cn/current/Manual/android-keystore-create.html)
  * [日本語](/ja/current/Manual/android-keystore-create.html)
  * [한국어](/kr/current/Manual/android-keystore-create.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/android-keystore-create.html)
  * [中文](/cn/current/Manual/android-keystore-create.html)
  * [日本語](/ja/current/Manual/android-keystore-create.html)
  * [한국어](/kr/current/Manual/android-keystore-create.html)

  * [Platform development ](PlatformSpecific.html)
  * [Android](android.html)
  * [Getting started with Android](android-getting-started.html)
  * [Android keystores](android-keystore.html)
  * Create a new keystore

[](android-keystore-manager.html)

Keystore Manager window reference

[](android-keystore-add-keys.html)

Add keys to a keystore

# Create a new keystore

This page explains how to use the Keystore Manager window to create a new
keystore.

This is relevant if you want to publish your application, because you must
provide a key from a keystore when you sign the application.

To create a new keystore:

  1. Open the [Keystore Manager window](android-keystore-manager.html).
  2. In the top-left of the window, select **Keystore** > **Create New**.
  3. Select **Anywhere** and save the keystore file in your Project folder, or select **In Dedicated Location** and save the keystore to a different directory on your computer. For more information, see Choose the keystore location.
  4. Enter a password for the keystore in the **Password** field and re-enter the password in the **Confirm password** field.
  5. A keystore must contain at least one key so to finish creating a keystore, add a key. To do this, see [Add keys to a keystore](android-keystore-add-keys.html).

## Choose the keystore location

You can create a new keystore anywhere on your computer, however there are two
special locations: the Project folder and what is called the keystores
dedicated location. If you place a keystore in either of these places, Unity
saves a relative path to the keystore. Otherwise Unity saves an absolute path
to the keystore. Under the **Keystore** > **Create New** menu option, there
are two options:

  * **Anywhere** opens the file explorer at the root of your project folder. This is the default place that Unity stores keystores.
  * **In Dedicated Location** opens the file explorer in a custom location. By default, this path points to `$HOME/` on MacOS and to `%USER_HOME%\` on Windows. To change the dedicated location for your computer, go to **Edit** > **Preferences** (macOS: **Unity > Settings**) and then navigate to **External Tools** > **Android** > **Keystores Dedicated Location**. Select **Browse** to choose a location or enter a path in the text box.

If you store a keystore in a dedicated location, Unity saves a relative path
from the dedicated location to the keystore. This means different computers
can specify a different dedicated location and store the keystore in a
different place.

**Note** : If you save the new keystore outside of your Project folder or a
shared directory, collaborators on your project might not have access to it.

## Additional resources

  * [Keystore Manager window reference](android-keystore-manager.html)
  * [Add keys to a keystore](android-keystore-add-keys.html)

[](android-keystore-manager.html)

Keystore Manager window reference

[](android-keystore-add-keys.html)

Add keys to a keystore

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

