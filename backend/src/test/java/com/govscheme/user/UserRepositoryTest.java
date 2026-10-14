package com.govscheme.user;

import com.govscheme.user.entity.User;
import com.govscheme.user.repository.UserRepository;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.data.jpa.test.autoconfigure.DataJpaTest;
import org.springframework.boot.jdbc.test.autoconfigure.AutoConfigureTestDatabase;
import org.springframework.test.context.ActiveProfiles;

import java.util.Optional;

import static org.assertj.core.api.Assertions.assertThat;

@DataJpaTest
@AutoConfigureTestDatabase(replace = AutoConfigureTestDatabase.Replace.NONE)
@ActiveProfiles("test")
class UserRepositoryTest {

    @Autowired
    private UserRepository userRepository;

    @Test
    void savesAndReloadsUserCorrectly() {

        // Arrange: Create a user
        User user = new User();
        user.setName("Test User");
        user.setEmail("test@example.com");
        user.setPasswordHash("hashed-password");
        user.setRole(User.Role.USER);

        // Act: Save the user
        User saved = userRepository.saveAndFlush(user);

        // Retrieve the user using email
        Optional<User> found =
                userRepository.findByEmail("test@example.com");

        // Assert: Verify the saved user
        assertThat(saved.getId()).isNotNull();

        assertThat(found).isPresent();

        assertThat(found.get().getId())
                .isEqualTo(saved.getId());

        assertThat(found.get().getName())
                .isEqualTo("Test User");

        assertThat(found.get().getEmail())
                .isEqualTo("test@example.com");
    }
}
