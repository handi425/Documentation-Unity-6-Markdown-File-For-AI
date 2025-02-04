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

# KeyCode

enumeration

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

[ ]()

### Description

Key codes returned by [Event.keyCode](Event-keyCode.html). These map directly
to a physical key on the keyboard. If "Use Physical Keys" is enabled in [Input
Manager settings](../Manual/class-InputManager.html), these map directly to a
physical key on the keyboard. If "Use Physical Keys" is disabled these map to
language dependent mapping, different for every platform and cannot be
guaranteed to work. "Use Physical Keys" is enabled by default from 2022.1

Key codes can be used to detect key down and key up events, using
[Input.GetKeyDown](Input.GetKeyDown.html) and
[Input.GetKeyUp](Input.GetKeyUp.html):

    
    
    using UnityEngine;  
      
    public class KeyCodeExample : [MonoBehaviour](MonoBehaviour.html)
    {
        void [Update](PlayerLoop.Update.html)()
        {
            if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.Space](KeyCode.Space.html)))
            {
                [Debug.Log](Debug.Log.html)("[Space](Space.html) key was pressed.");
            }  
      
            if ([Input.GetKeyUp](Input.GetKeyUp.html)([KeyCode.Space](KeyCode.Space.html)))
            {
                [Debug.Log](Debug.Log.html)("[Space](Space.html) key was released.");
            }
        }
    }
    

Keyboard events can also be captured within `OnGUI`:

    
    
    using UnityEngine;  
      
    public class KeyCodeOnGUIExample : [MonoBehaviour](MonoBehaviour.html)
    {
        void OnGUI()
        {
            if (Event.current.Equals([Event.KeyboardEvent](Event.KeyboardEvent.html)(KeyCode.Space.ToString())))
            {
                [Debug.Log](Debug.Log.html)("[Space](Space.html) key is pressed.");
            }
        }
    }
    

For joystick and gamepad button presses, consider using
[Input.GetButtonDown](Input.GetButtonDown.html) and
[Input.GetButtonUp](Input.GetButtonUp.html) instead of the KeyCode. These
methods allow you to check input state using a descriptive action string, e.g.
"fire" or "jump", instead of the hardware button number.  
  
The [Input](Input.html) pages provide details about accessing keyboard, mouse
and joystick input.

### Properties

[None](KeyCode.None.html)| Not assigned (never returned as the result of a
keystroke).  
---|---  
[Backspace](KeyCode.Backspace.html)| The backspace key.  
[Delete](KeyCode.Delete.html)| The forward delete key.  
[Tab](KeyCode.Tab.html)| The tab key.  
[Clear](KeyCode.Clear.html)| The Clear key.  
[Return](KeyCode.Return.html)| Return key.  
[Pause](KeyCode.Pause.html)| Pause on PC machines.  
[Escape](KeyCode.Escape.html)| Escape key.  
[Space](KeyCode.Space.html)| Space key.  
[Keypad0](KeyCode.Keypad0.html)| Numeric keypad 0.  
[Keypad1](KeyCode.Keypad1.html)| Numeric keypad 1.  
[Keypad2](KeyCode.Keypad2.html)| Numeric keypad 2.  
[Keypad3](KeyCode.Keypad3.html)| Numeric keypad 3.  
[Keypad4](KeyCode.Keypad4.html)| Numeric keypad 4.  
[Keypad5](KeyCode.Keypad5.html)| Numeric keypad 5.  
[Keypad6](KeyCode.Keypad6.html)| Numeric keypad 6.  
[Keypad7](KeyCode.Keypad7.html)| Numeric keypad 7.  
[Keypad8](KeyCode.Keypad8.html)| Numeric keypad 8.  
[Keypad9](KeyCode.Keypad9.html)| Numeric keypad 9.  
[KeypadPeriod](KeyCode.KeypadPeriod.html)| Numeric keypad '.'.  
[KeypadDivide](KeyCode.KeypadDivide.html)| Numeric keypad '/'.  
[KeypadMultiply](KeyCode.KeypadMultiply.html)| Numeric keypad '*'.  
[KeypadMinus](KeyCode.KeypadMinus.html)| Numeric keypad '-'.  
[KeypadPlus](KeyCode.KeypadPlus.html)| Numeric keypad '+'.  
[KeypadEnter](KeyCode.KeypadEnter.html)| Numeric keypad Enter.  
[KeypadEquals](KeyCode.KeypadEquals.html)| Numeric keypad '='.  
[UpArrow](KeyCode.UpArrow.html)| Up arrow key.  
[DownArrow](KeyCode.DownArrow.html)| Down arrow key.  
[RightArrow](KeyCode.RightArrow.html)| Right arrow key.  
[LeftArrow](KeyCode.LeftArrow.html)| Left arrow key.  
[Insert](KeyCode.Insert.html)| Insert key key.  
[Home](KeyCode.Home.html)| Home key.  
[End](KeyCode.End.html)| End key.  
[PageUp](KeyCode.PageUp.html)| Page up.  
[PageDown](KeyCode.PageDown.html)| Page down.  
[F1](KeyCode.F1.html)| F1 function key.  
[F2](KeyCode.F2.html)| F2 function key.  
[F3](KeyCode.F3.html)| F3 function key.  
[F4](KeyCode.F4.html)| F4 function key.  
[F5](KeyCode.F5.html)| F5 function key.  
[F6](KeyCode.F6.html)| F6 function key.  
[F7](KeyCode.F7.html)| F7 function key.  
[F8](KeyCode.F8.html)| F8 function key.  
[F9](KeyCode.F9.html)| F9 function key.  
[F10](KeyCode.F10.html)| F10 function key.  
[F11](KeyCode.F11.html)| F11 function key.  
[F12](KeyCode.F12.html)| F12 function key.  
[F13](KeyCode.F13.html)| F13 function key.  
[F14](KeyCode.F14.html)| F14 function key.  
[F15](KeyCode.F15.html)| F15 function key.  
[Alpha0](KeyCode.Alpha0.html)| The '0' key on the top of the alphanumeric
keyboard.  
[Alpha1](KeyCode.Alpha1.html)| The '1' key on the top of the alphanumeric
keyboard.  
[Alpha2](KeyCode.Alpha2.html)| The '2' key on the top of the alphanumeric
keyboard.  
[Alpha3](KeyCode.Alpha3.html)| The '3' key on the top of the alphanumeric
keyboard.  
[Alpha4](KeyCode.Alpha4.html)| The '4' key on the top of the alphanumeric
keyboard.  
[Alpha5](KeyCode.Alpha5.html)| The '5' key on the top of the alphanumeric
keyboard.  
[Alpha6](KeyCode.Alpha6.html)| The '6' key on the top of the alphanumeric
keyboard.  
[Alpha7](KeyCode.Alpha7.html)| The '7' key on the top of the alphanumeric
keyboard.  
[Alpha8](KeyCode.Alpha8.html)| The '8' key on the top of the alphanumeric
keyboard.  
[Alpha9](KeyCode.Alpha9.html)| The '9' key on the top of the alphanumeric
keyboard.  
[Exclaim](KeyCode.Exclaim.html)| Exclamation mark key '!'. Deprecated if "Use
Physical Keys" is enabled in Input Manager settings, use KeyCode.Alpha1
instead.  
[DoubleQuote](KeyCode.DoubleQuote.html)| Double quote key '"'. Deprecated if
"Use Physical Keys" is enabled in Input Manager settings, use KeyCode.Quote
instead.  
[Hash](KeyCode.Hash.html)| Hash key '#'. Deprecated if "Use Physical Keys" is
enabled in Input Manager settings, use KeyCode.Alpha3 instead.  
[Dollar](KeyCode.Dollar.html)| Dollar sign key '$'. Deprecated if "Use
Physical Keys" is enabled in Input Manager settings, use KeyCode.Alpha4
instead.  
[Percent](KeyCode.Percent.html)| Percent '%' key. Deprecated if "Use Physical
Keys" is enabled in Input Manager settings, use KeyCode.Alpha5 instead.  
[Ampersand](KeyCode.Ampersand.html)| Ampersand key '&'. Deprecated if "Use
Physical Keys" is enabled in Input Manager settings, use KeyCode.Alpha7
instead.  
[Quote](KeyCode.Quote.html)| Quote key '.  
[LeftParen](KeyCode.LeftParen.html)| Left Parenthesis key '('. Deprecated if
"Use Physical Keys" is enabled in Input Manager settings, use KeyCode.Alpha9
instead.  
[RightParen](KeyCode.RightParen.html)| Right Parenthesis key ')'. Deprecated
if "Use Physical Keys" is enabled in Input Manager settings, use
KeyCode.Alpha0 instead.  
[Asterisk](KeyCode.Asterisk.html)| Asterisk key '*'. Deprecated if "Use
Physical Keys" is enabled in Input Manager settings, use KeyCode.Alpha8
instead.  
[Plus](KeyCode.Plus.html)| Plus key '+'. Deprecated if "Use Physical Keys" is
enabled in Input Manager settings, use KeyCode.Equals instead.  
[Comma](KeyCode.Comma.html)| Comma ',' key.  
[Minus](KeyCode.Minus.html)| Minus '-' key.  
[Period](KeyCode.Period.html)| Period '.' key.  
[Slash](KeyCode.Slash.html)| Slash '/' key.  
[Colon](KeyCode.Colon.html)| Colon ':' key.Deprecated if "Use Physical Keys"
is enabled in Input Manager settings, use KeyCode.Semicolon instead.  
[Semicolon](KeyCode.Semicolon.html)| Semicolon ';' key.  
[Less](KeyCode.Less.html)| Less than '<' key. Deprecated if "Use Physical
Keys" is enabled in Input Manager settings, use KeyCode.Comma instead.  
[Equals](KeyCode.Equals.html)| Equals '=' key.  
[Greater](KeyCode.Greater.html)| Greater than '>' key. Deprecated if "Use
Physical Keys" is enabled in Input Manager settings, use KeyCode.Period
instead.  
[Question](KeyCode.Question.html)| Question mark '?' key. Deprecated if "Use
Physical Keys" is enabled in Input Manager settings, use KeyCode.Slash
instead.  
[At](KeyCode.At.html)| At key '@'. Deprecated if "Use Physical Keys" is
enabled in Input Manager settings, use KeyCode.Alpha2 instead.  
[LeftBracket](KeyCode.LeftBracket.html)| Left square bracket key '['.  
[Backslash](KeyCode.Backslash.html)| Backslash key '\'.  
[RightBracket](KeyCode.RightBracket.html)| Right square bracket key ']'.  
[Caret](KeyCode.Caret.html)| Caret key '^'. Deprecated if "Use Physical Keys"
is enabled in Input Manager settings, use KeyCode.Alpha6 instead.  
[Underscore](KeyCode.Underscore.html)| Underscore '_' key. Deprecated if "Use
Physical Keys" is enabled in Input Manager settings, use KeyCode.Minus
instead.  
[BackQuote](KeyCode.BackQuote.html)| Back quote key '`'.  
[A](KeyCode.A.html)| 'a' key.  
[B](KeyCode.B.html)| 'b' key.  
[C](KeyCode.C.html)| 'c' key.  
[D](KeyCode.D.html)| 'd' key.  
[E](KeyCode.E.html)| 'e' key.  
[F](KeyCode.F.html)| 'f' key.  
[G](KeyCode.G.html)| 'g' key.  
[H](KeyCode.H.html)| 'h' key.  
[I](KeyCode.I.html)| 'i' key.  
[J](KeyCode.J.html)| 'j' key.  
[K](KeyCode.K.html)| 'k' key.  
[L](KeyCode.L.html)| 'l' key.  
[M](KeyCode.M.html)| 'm' key.  
[N](KeyCode.N.html)| 'n' key.  
[O](KeyCode.O.html)| 'o' key.  
[P](KeyCode.P.html)| 'p' key.  
[Q](KeyCode.Q.html)| 'q' key.  
[R](KeyCode.R.html)| 'r' key.  
[S](KeyCode.S.html)| 's' key.  
[T](KeyCode.T.html)| 't' key.  
[U](KeyCode.U.html)| 'u' key.  
[V](KeyCode.V.html)| 'v' key.  
[W](KeyCode.W.html)| 'w' key.  
[X](KeyCode.X.html)| 'x' key.  
[Y](KeyCode.Y.html)| 'y' key.  
[Z](KeyCode.Z.html)| 'z' key.  
[LeftCurlyBracket](KeyCode.LeftCurlyBracket.html)| Left curly bracket key '{'.
Deprecated if "Use Physical Keys" is enabled in Input Manager settings, use
KeyCode.LeftBracket instead.  
[Pipe](KeyCode.Pipe.html)| Pipe '|' key. Deprecated if "Use Physical Keys" is
enabled in Input Manager settings, use KeyCode.Backslash instead.  
[RightCurlyBracket](KeyCode.RightCurlyBracket.html)| Right curly bracket key
'}'. Deprecated if "Use Physical Keys" is enabled in Input Manager settings,
use KeyCode.RightBracket instead.  
[Tilde](KeyCode.Tilde.html)| Tilde '~' key. Deprecated if "Use Physical Keys"
is enabled in Input Manager settings, use KeyCode.BackQuote instead.  
[Numlock](KeyCode.Numlock.html)| Numlock key.  
[CapsLock](KeyCode.CapsLock.html)| Capslock key.  
[ScrollLock](KeyCode.ScrollLock.html)| Scroll lock key.  
[RightShift](KeyCode.RightShift.html)| Right shift key.  
[LeftShift](KeyCode.LeftShift.html)| Left shift key.  
[RightControl](KeyCode.RightControl.html)| Right Control key.  
[LeftControl](KeyCode.LeftControl.html)| Left Control key.  
[RightAlt](KeyCode.RightAlt.html)| Right Alt key.  
[LeftAlt](KeyCode.LeftAlt.html)| Left Alt key.  
[LeftMeta](KeyCode.LeftMeta.html)| Maps to left Windows key or left Command
key if physical keys are enabled in Input Manager settings, otherwise maps to
left Command key only.  
[LeftCommand](KeyCode.LeftCommand.html)| Left Command key.  
[LeftApple](KeyCode.LeftApple.html)| Left Command key.  
[LeftWindows](KeyCode.LeftWindows.html)| Left Windows key. Deprecated if "Use
Physical Keys" is enabled in Input Manager settings, use KeyCode.LeftMeta
instead.  
[RightMeta](KeyCode.RightMeta.html)| Maps to right Windows key or right
Command key if physical keys are enabled in Input Manager settings, otherwise
maps to right Command key only.  
[RightCommand](KeyCode.RightCommand.html)| Right Command key.  
[RightApple](KeyCode.RightApple.html)| Right Command key.  
[RightWindows](KeyCode.RightWindows.html)| Right Windows key. Deprecated if
"Use Physical Keys" is enabled in Input Manager settings, use
KeyCode.RightMeta instead.  
[AltGr](KeyCode.AltGr.html)| Alt Gr key. Deprecated if "Use Physical Keys" is
enabled in Input Manager settings, use KeyCode.RightAlt instead.  
[Help](KeyCode.Help.html)| Help key. Deprecated if "Use Physical Keys" is
enabled in Input Manager settings, doesn't map to any physical key.  
[Print](KeyCode.Print.html)| Print key.  
[SysReq](KeyCode.SysReq.html)| Sys Req key. Deprecated if "Use Physical Keys"
is enabled in Input Manager settings, doesn't map to any physical key.  
[Break](KeyCode.Break.html)| Break key. Deprecated if "Use Physical Keys" is
enabled in Input Manager settings, doesn't map to any physical key.  
[Menu](KeyCode.Menu.html)| Menu key.  
[WheelUp](KeyCode.WheelUp.html)| Mouse wheel up.  
[WheelDown](KeyCode.WheelDown.html)| Mouse wheel down.  
[Mouse0](KeyCode.Mouse0.html)| The Left (or primary) mouse button.  
[Mouse1](KeyCode.Mouse1.html)| Right mouse button (or secondary mouse button).  
[Mouse2](KeyCode.Mouse2.html)| Middle mouse button (or third button).  
[Mouse3](KeyCode.Mouse3.html)| Additional (fourth) mouse button.  
[Mouse4](KeyCode.Mouse4.html)| Additional (fifth) mouse button.  
[Mouse5](KeyCode.Mouse5.html)| Additional (or sixth) mouse button.  
[Mouse6](KeyCode.Mouse6.html)| Additional (or seventh) mouse button.  
[JoystickButton0](KeyCode.JoystickButton0.html)| Button 0 on any joystick.  
[JoystickButton1](KeyCode.JoystickButton1.html)| Button 1 on any joystick.  
[JoystickButton2](KeyCode.JoystickButton2.html)| Button 2 on any joystick.  
[JoystickButton3](KeyCode.JoystickButton3.html)| Button 3 on any joystick.  
[JoystickButton4](KeyCode.JoystickButton4.html)| Button 4 on any joystick.  
[JoystickButton5](KeyCode.JoystickButton5.html)| Button 5 on any joystick.  
[JoystickButton6](KeyCode.JoystickButton6.html)| Button 6 on any joystick.  
[JoystickButton7](KeyCode.JoystickButton7.html)| Button 7 on any joystick.  
[JoystickButton8](KeyCode.JoystickButton8.html)| Button 8 on any joystick.  
[JoystickButton9](KeyCode.JoystickButton9.html)| Button 9 on any joystick.  
[JoystickButton10](KeyCode.JoystickButton10.html)| Button 10 on any joystick.  
[JoystickButton11](KeyCode.JoystickButton11.html)| Button 11 on any joystick.  
[JoystickButton12](KeyCode.JoystickButton12.html)| Button 12 on any joystick.  
[JoystickButton13](KeyCode.JoystickButton13.html)| Button 13 on any joystick.  
[JoystickButton14](KeyCode.JoystickButton14.html)| Button 14 on any joystick.  
[JoystickButton15](KeyCode.JoystickButton15.html)| Button 15 on any joystick.  
[JoystickButton16](KeyCode.JoystickButton16.html)| Button 16 on any joystick.  
[JoystickButton17](KeyCode.JoystickButton17.html)| Button 17 on any joystick.  
[JoystickButton18](KeyCode.JoystickButton18.html)| Button 18 on any joystick.  
[JoystickButton19](KeyCode.JoystickButton19.html)| Button 19 on any joystick.  
[Joystick1Button0](KeyCode.Joystick1Button0.html)| Button 0 on first joystick.  
[Joystick1Button1](KeyCode.Joystick1Button1.html)| Button 1 on first joystick.  
[Joystick1Button2](KeyCode.Joystick1Button2.html)| Button 2 on first joystick.  
[Joystick1Button3](KeyCode.Joystick1Button3.html)| Button 3 on first joystick.  
[Joystick1Button4](KeyCode.Joystick1Button4.html)| Button 4 on first joystick.  
[Joystick1Button5](KeyCode.Joystick1Button5.html)| Button 5 on first joystick.  
[Joystick1Button6](KeyCode.Joystick1Button6.html)| Button 6 on first joystick.  
[Joystick1Button7](KeyCode.Joystick1Button7.html)| Button 7 on first joystick.  
[Joystick1Button8](KeyCode.Joystick1Button8.html)| Button 8 on first joystick.  
[Joystick1Button9](KeyCode.Joystick1Button9.html)| Button 9 on first joystick.  
[Joystick1Button10](KeyCode.Joystick1Button10.html)| Button 10 on first
joystick.  
[Joystick1Button11](KeyCode.Joystick1Button11.html)| Button 11 on first
joystick.  
[Joystick1Button12](KeyCode.Joystick1Button12.html)| Button 12 on first
joystick.  
[Joystick1Button13](KeyCode.Joystick1Button13.html)| Button 13 on first
joystick.  
[Joystick1Button14](KeyCode.Joystick1Button14.html)| Button 14 on first
joystick.  
[Joystick1Button15](KeyCode.Joystick1Button15.html)| Button 15 on first
joystick.  
[Joystick1Button16](KeyCode.Joystick1Button16.html)| Button 16 on first
joystick.  
[Joystick1Button17](KeyCode.Joystick1Button17.html)| Button 17 on first
joystick.  
[Joystick1Button18](KeyCode.Joystick1Button18.html)| Button 18 on first
joystick.  
[Joystick1Button19](KeyCode.Joystick1Button19.html)| Button 19 on first
joystick.  
[Joystick2Button0](KeyCode.Joystick2Button0.html)| Button 0 on second
joystick.  
[Joystick2Button1](KeyCode.Joystick2Button1.html)| Button 1 on second
joystick.  
[Joystick2Button2](KeyCode.Joystick2Button2.html)| Button 2 on second
joystick.  
[Joystick2Button3](KeyCode.Joystick2Button3.html)| Button 3 on second
joystick.  
[Joystick2Button4](KeyCode.Joystick2Button4.html)| Button 4 on second
joystick.  
[Joystick2Button5](KeyCode.Joystick2Button5.html)| Button 5 on second
joystick.  
[Joystick2Button6](KeyCode.Joystick2Button6.html)| Button 6 on second
joystick.  
[Joystick2Button7](KeyCode.Joystick2Button7.html)| Button 7 on second
joystick.  
[Joystick2Button8](KeyCode.Joystick2Button8.html)| Button 8 on second
joystick.  
[Joystick2Button9](KeyCode.Joystick2Button9.html)| Button 9 on second
joystick.  
[Joystick2Button10](KeyCode.Joystick2Button10.html)| Button 10 on second
joystick.  
[Joystick2Button11](KeyCode.Joystick2Button11.html)| Button 11 on second
joystick.  
[Joystick2Button12](KeyCode.Joystick2Button12.html)| Button 12 on second
joystick.  
[Joystick2Button13](KeyCode.Joystick2Button13.html)| Button 13 on second
joystick.  
[Joystick2Button14](KeyCode.Joystick2Button14.html)| Button 14 on second
joystick.  
[Joystick2Button15](KeyCode.Joystick2Button15.html)| Button 15 on second
joystick.  
[Joystick2Button16](KeyCode.Joystick2Button16.html)| Button 16 on second
joystick.  
[Joystick2Button17](KeyCode.Joystick2Button17.html)| Button 17 on second
joystick.  
[Joystick2Button18](KeyCode.Joystick2Button18.html)| Button 18 on second
joystick.  
[Joystick2Button19](KeyCode.Joystick2Button19.html)| Button 19 on second
joystick.  
[Joystick3Button0](KeyCode.Joystick3Button0.html)| Button 0 on third joystick.  
[Joystick3Button1](KeyCode.Joystick3Button1.html)| Button 1 on third joystick.  
[Joystick3Button2](KeyCode.Joystick3Button2.html)| Button 2 on third joystick.  
[Joystick3Button3](KeyCode.Joystick3Button3.html)| Button 3 on third joystick.  
[Joystick3Button4](KeyCode.Joystick3Button4.html)| Button 4 on third joystick.  
[Joystick3Button5](KeyCode.Joystick3Button5.html)| Button 5 on third joystick.  
[Joystick3Button6](KeyCode.Joystick3Button6.html)| Button 6 on third joystick.  
[Joystick3Button7](KeyCode.Joystick3Button7.html)| Button 7 on third joystick.  
[Joystick3Button8](KeyCode.Joystick3Button8.html)| Button 8 on third joystick.  
[Joystick3Button9](KeyCode.Joystick3Button9.html)| Button 9 on third joystick.  
[Joystick3Button10](KeyCode.Joystick3Button10.html)| Button 10 on third
joystick.  
[Joystick3Button11](KeyCode.Joystick3Button11.html)| Button 11 on third
joystick.  
[Joystick3Button12](KeyCode.Joystick3Button12.html)| Button 12 on third
joystick.  
[Joystick3Button13](KeyCode.Joystick3Button13.html)| Button 13 on third
joystick.  
[Joystick3Button14](KeyCode.Joystick3Button14.html)| Button 14 on third
joystick.  
[Joystick3Button15](KeyCode.Joystick3Button15.html)| Button 15 on third
joystick.  
[Joystick3Button16](KeyCode.Joystick3Button16.html)| Button 16 on third
joystick.  
[Joystick3Button17](KeyCode.Joystick3Button17.html)| Button 17 on third
joystick.  
[Joystick3Button18](KeyCode.Joystick3Button18.html)| Button 18 on third
joystick.  
[Joystick3Button19](KeyCode.Joystick3Button19.html)| Button 19 on third
joystick.  
[Joystick4Button0](KeyCode.Joystick4Button0.html)| Button 0 on forth joystick.  
[Joystick4Button1](KeyCode.Joystick4Button1.html)| Button 1 on forth joystick.  
[Joystick4Button2](KeyCode.Joystick4Button2.html)| Button 2 on forth joystick.  
[Joystick4Button3](KeyCode.Joystick4Button3.html)| Button 3 on forth joystick.  
[Joystick4Button4](KeyCode.Joystick4Button4.html)| Button 4 on forth joystick.  
[Joystick4Button5](KeyCode.Joystick4Button5.html)| Button 5 on forth joystick.  
[Joystick4Button6](KeyCode.Joystick4Button6.html)| Button 6 on forth joystick.  
[Joystick4Button7](KeyCode.Joystick4Button7.html)| Button 7 on forth joystick.  
[Joystick4Button8](KeyCode.Joystick4Button8.html)| Button 8 on forth joystick.  
[Joystick4Button9](KeyCode.Joystick4Button9.html)| Button 9 on forth joystick.  
[Joystick4Button10](KeyCode.Joystick4Button10.html)| Button 10 on forth
joystick.  
[Joystick4Button11](KeyCode.Joystick4Button11.html)| Button 11 on forth
joystick.  
[Joystick4Button12](KeyCode.Joystick4Button12.html)| Button 12 on forth
joystick.  
[Joystick4Button13](KeyCode.Joystick4Button13.html)| Button 13 on forth
joystick.  
[Joystick4Button14](KeyCode.Joystick4Button14.html)| Button 14 on forth
joystick.  
[Joystick4Button15](KeyCode.Joystick4Button15.html)| Button 15 on forth
joystick.  
[Joystick4Button16](KeyCode.Joystick4Button16.html)| Button 16 on forth
joystick.  
[Joystick4Button17](KeyCode.Joystick4Button17.html)| Button 17 on forth
joystick.  
[Joystick4Button18](KeyCode.Joystick4Button18.html)| Button 18 on forth
joystick.  
[Joystick4Button19](KeyCode.Joystick4Button19.html)| Button 19 on forth
joystick.  
[Joystick5Button0](KeyCode.Joystick5Button0.html)| Button 0 on fifth joystick.  
[Joystick5Button1](KeyCode.Joystick5Button1.html)| Button 1 on fifth joystick.  
[Joystick5Button2](KeyCode.Joystick5Button2.html)| Button 2 on fifth joystick.  
[Joystick5Button3](KeyCode.Joystick5Button3.html)| Button 3 on fifth joystick.  
[Joystick5Button4](KeyCode.Joystick5Button4.html)| Button 4 on fifth joystick.  
[Joystick5Button5](KeyCode.Joystick5Button5.html)| Button 5 on fifth joystick.  
[Joystick5Button6](KeyCode.Joystick5Button6.html)| Button 6 on fifth joystick.  
[Joystick5Button7](KeyCode.Joystick5Button7.html)| Button 7 on fifth joystick.  
[Joystick5Button8](KeyCode.Joystick5Button8.html)| Button 8 on fifth joystick.  
[Joystick5Button9](KeyCode.Joystick5Button9.html)| Button 9 on fifth joystick.  
[Joystick5Button10](KeyCode.Joystick5Button10.html)| Button 10 on fifth
joystick.  
[Joystick5Button11](KeyCode.Joystick5Button11.html)| Button 11 on fifth
joystick.  
[Joystick5Button12](KeyCode.Joystick5Button12.html)| Button 12 on fifth
joystick.  
[Joystick5Button13](KeyCode.Joystick5Button13.html)| Button 13 on fifth
joystick.  
[Joystick5Button14](KeyCode.Joystick5Button14.html)| Button 14 on fifth
joystick.  
[Joystick5Button15](KeyCode.Joystick5Button15.html)| Button 15 on fifth
joystick.  
[Joystick5Button16](KeyCode.Joystick5Button16.html)| Button 16 on fifth
joystick.  
[Joystick5Button17](KeyCode.Joystick5Button17.html)| Button 17 on fifth
joystick.  
[Joystick5Button18](KeyCode.Joystick5Button18.html)| Button 18 on fifth
joystick.  
[Joystick5Button19](KeyCode.Joystick5Button19.html)| Button 19 on fifth
joystick.  
[Joystick6Button0](KeyCode.Joystick6Button0.html)| Button 0 on sixth joystick.  
[Joystick6Button1](KeyCode.Joystick6Button1.html)| Button 1 on sixth joystick.  
[Joystick6Button2](KeyCode.Joystick6Button2.html)| Button 2 on sixth joystick.  
[Joystick6Button3](KeyCode.Joystick6Button3.html)| Button 3 on sixth joystick.  
[Joystick6Button4](KeyCode.Joystick6Button4.html)| Button 4 on sixth joystick.  
[Joystick6Button5](KeyCode.Joystick6Button5.html)| Button 5 on sixth joystick.  
[Joystick6Button6](KeyCode.Joystick6Button6.html)| Button 6 on sixth joystick.  
[Joystick6Button7](KeyCode.Joystick6Button7.html)| Button 7 on sixth joystick.  
[Joystick6Button8](KeyCode.Joystick6Button8.html)| Button 8 on sixth joystick.  
[Joystick6Button9](KeyCode.Joystick6Button9.html)| Button 9 on sixth joystick.  
[Joystick6Button10](KeyCode.Joystick6Button10.html)| Button 10 on sixth
joystick.  
[Joystick6Button11](KeyCode.Joystick6Button11.html)| Button 11 on sixth
joystick.  
[Joystick6Button12](KeyCode.Joystick6Button12.html)| Button 12 on sixth
joystick.  
[Joystick6Button13](KeyCode.Joystick6Button13.html)| Button 13 on sixth
joystick.  
[Joystick6Button14](KeyCode.Joystick6Button14.html)| Button 14 on sixth
joystick.  
[Joystick6Button15](KeyCode.Joystick6Button15.html)| Button 15 on sixth
joystick.  
[Joystick6Button16](KeyCode.Joystick6Button16.html)| Button 16 on sixth
joystick.  
[Joystick6Button17](KeyCode.Joystick6Button17.html)| Button 17 on sixth
joystick.  
[Joystick6Button18](KeyCode.Joystick6Button18.html)| Button 18 on sixth
joystick.  
[Joystick6Button19](KeyCode.Joystick6Button19.html)| Button 19 on sixth
joystick.  
[Joystick7Button0](KeyCode.Joystick7Button0.html)| Button 0 on seventh
joystick.  
[Joystick7Button1](KeyCode.Joystick7Button1.html)| Button 1 on seventh
joystick.  
[Joystick7Button2](KeyCode.Joystick7Button2.html)| Button 2 on seventh
joystick.  
[Joystick7Button3](KeyCode.Joystick7Button3.html)| Button 3 on seventh
joystick.  
[Joystick7Button4](KeyCode.Joystick7Button4.html)| Button 4 on seventh
joystick.  
[Joystick7Button5](KeyCode.Joystick7Button5.html)| Button 5 on seventh
joystick.  
[Joystick7Button6](KeyCode.Joystick7Button6.html)| Button 6 on seventh
joystick.  
[Joystick7Button7](KeyCode.Joystick7Button7.html)| Button 7 on seventh
joystick.  
[Joystick7Button8](KeyCode.Joystick7Button8.html)| Button 8 on seventh
joystick.  
[Joystick7Button9](KeyCode.Joystick7Button9.html)| Button 9 on seventh
joystick.  
[Joystick7Button10](KeyCode.Joystick7Button10.html)| Button 10 on seventh
joystick.  
[Joystick7Button11](KeyCode.Joystick7Button11.html)| Button 11 on seventh
joystick.  
[Joystick7Button12](KeyCode.Joystick7Button12.html)| Button 12 on seventh
joystick.  
[Joystick7Button13](KeyCode.Joystick7Button13.html)| Button 13 on seventh
joystick.  
[Joystick7Button14](KeyCode.Joystick7Button14.html)| Button 14 on seventh
joystick.  
[Joystick7Button15](KeyCode.Joystick7Button15.html)| Button 15 on seventh
joystick.  
[Joystick7Button16](KeyCode.Joystick7Button16.html)| Button 16 on seventh
joystick.  
[Joystick7Button17](KeyCode.Joystick7Button17.html)| Button 17 on seventh
joystick.  
[Joystick7Button18](KeyCode.Joystick7Button18.html)| Button 18 on seventh
joystick.  
[Joystick7Button19](KeyCode.Joystick7Button19.html)| Button 19 on seventh
joystick.  
[Joystick8Button0](KeyCode.Joystick8Button0.html)| Button 0 on eighth
joystick.  
[Joystick8Button1](KeyCode.Joystick8Button1.html)| Button 1 on eighth
joystick.  
[Joystick8Button2](KeyCode.Joystick8Button2.html)| Button 2 on eighth
joystick.  
[Joystick8Button3](KeyCode.Joystick8Button3.html)| Button 3 on eighth
joystick.  
[Joystick8Button4](KeyCode.Joystick8Button4.html)| Button 4 on eighth
joystick.  
[Joystick8Button5](KeyCode.Joystick8Button5.html)| Button 5 on eighth
joystick.  
[Joystick8Button6](KeyCode.Joystick8Button6.html)| Button 6 on eighth
joystick.  
[Joystick8Button7](KeyCode.Joystick8Button7.html)| Button 7 on eighth
joystick.  
[Joystick8Button8](KeyCode.Joystick8Button8.html)| Button 8 on eighth
joystick.  
[Joystick8Button9](KeyCode.Joystick8Button9.html)| Button 9 on eighth
joystick.  
[Joystick8Button10](KeyCode.Joystick8Button10.html)| Button 10 on eighth
joystick.  
[Joystick8Button11](KeyCode.Joystick8Button11.html)| Button 11 on eighth
joystick.  
[Joystick8Button12](KeyCode.Joystick8Button12.html)| Button 12 on eighth
joystick.  
[Joystick8Button13](KeyCode.Joystick8Button13.html)| Button 13 on eighth
joystick.  
[Joystick8Button14](KeyCode.Joystick8Button14.html)| Button 14 on eighth
joystick.  
[Joystick8Button15](KeyCode.Joystick8Button15.html)| Button 15 on eighth
joystick.  
[Joystick8Button16](KeyCode.Joystick8Button16.html)| Button 16 on eighth
joystick.  
[Joystick8Button17](KeyCode.Joystick8Button17.html)| Button 17 on eighth
joystick.  
[Joystick8Button18](KeyCode.Joystick8Button18.html)| Button 18 on eighth
joystick.  
[Joystick8Button19](KeyCode.Joystick8Button19.html)| Button 19 on eighth
joystick.  
  
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

